from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("menu/", views.menu, name="menu"),
    path("menu_item/<int:item_id>/", views.menu_item, name="menu_item"),
    path("about/", views.about, name="about"),
]
