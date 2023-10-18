from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import formset_factory
from .forms import ShipForm, SpeedForm
from .models import Speed, Ship


def index(request):
    return HttpResponse("Hello, world. You're at the ships index.")


def ship_list(request):
    ships = Ship.objects.all()
    return render(request, "ship_list.html", {"ships": ships})


def check_for_speed(form):
    required_fields = [
        "name",
        "speed_in_kn",
        "consumption_main",
        "consumption_additional",
    ]
    return any(form.cleaned_data.get(field) for field in required_fields)


def create_speed_object(form, ship):
    data = form.cleaned_data
    Speed.objects.create(
        name=data["name"],
        speed_in_kn=data["speed_in_kn"],
        consumption_main=data["consumption_main"],
        consumption_additional=data["consumption_additional"],
        ship=ship,
    )


def add_ship(request):
    SpeedFormSet = formset_factory(SpeedForm, extra=4)

    if request.method == "POST":
        ship_form = ShipForm(request.POST)
        speed_formset = SpeedFormSet(request.POST)

        if ship_form.is_valid() and speed_formset.is_valid():
            ship = ship_form.save(commit=False)
            ship.name = ship_form.cleaned_data["name"].upper()
            ship.save()

            for form in speed_formset:
                if check_for_speed(form):
                    create_speed_object(form, ship)

            return redirect("ship_list")

    ship_form = ShipForm()
    speed_formset = SpeedFormSet()

    return render(
        request,
        "add_ship.html",
        {"ship_form": ship_form, "speed_formset": speed_formset},
    )


def add_speed(request):
    if request.method == "POST":
        speed_form = SpeedForm(request.POST)

        if speed_form.is_valid():
            speed = speed_form.save(commit=False)
            speed.save()
            return redirect("speed_list")
    else:
        speed_form = SpeedForm()

    return render(request, "add_speed.html", {"speed_form": speed_form})
