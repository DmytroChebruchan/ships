# urls.py
from django.urls import path
from .views import add_ship, ship_list

urlpatterns = [
    path("add_ship/", add_ship, name="add_ship"),
    path("ship_list/", ship_list, name="ship_list"),
]
