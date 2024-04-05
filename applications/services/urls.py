"""
URL configuration for services app.
"""

from django.urls import path

from . import views

app_name = "services"

urlpatterns = [
    path("", views.index, name="home"),
    path("details/<slug:slug>/", views.services_details, name="details"),
]
