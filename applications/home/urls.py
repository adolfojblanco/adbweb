"""
    URL configuration for home app.
"""
from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='index'),
    path('contacto', views.create_post, name='contact'),
]
