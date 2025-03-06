from django.urls import path
from . import views

urlpatterns = [
    path("", views.hellotime, name="hellotime"),
    path("screenprint", views.screenprint, name="screenprint"),
    path("blackbox", views.blackbox, name="blackbox"),
    path("aboutme", views.aboutme, name="aboutme"),
]