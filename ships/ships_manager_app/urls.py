# urls.py
from django.urls import path
from .views import add_ship, index, ship_list

urlpatterns = [
    path("", index, name="index_page"),
    path("add_ship/", add_ship, name="add_ship"),
    path("ship_list/", ship_list, name="ship_list"),
]
