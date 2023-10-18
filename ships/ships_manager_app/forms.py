# forms.py
from django import forms

from .models import Ship, Speed


class ShipForm(forms.ModelForm):
    class Meta:
        model = Ship
        fields = ["name", "year_of_built"]


class SpeedForm(forms.ModelForm):
    class Meta:
        model = Speed
        fields = [
            "name",
            "speed_in_kn",
            "consumption_main",
            "consumption_additional",
            "ship",
        ]
