"""
URL configuration for adbweb project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("applications.home.urls", namespace="home")),
    path("blog/", include("applications.blog.urls", namespace="blog")),
    path("projects/", include("applications.projects.urls", namespace="projects")),
    path("services/", include("applications.services.urls", namespace="services")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
