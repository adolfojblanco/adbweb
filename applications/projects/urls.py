"""
    URL configuration for projects app.
"""

from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.list, name='list'),
    path('detail', views.details, name='detail'),
]
