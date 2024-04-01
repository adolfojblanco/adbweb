"""
    URL configuration for adbweb project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('applications.home.urls')),
    path('blog', include('applications.blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
]
