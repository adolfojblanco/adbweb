"""
    URL configuration for home app.
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto', views.create_post, name='contact'),
]
