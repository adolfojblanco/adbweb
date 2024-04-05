from django.urls import path

from .views import post_details, posts_lists

app_name = "blog"

urlpatterns = [
    path("", posts_lists, name="posts_list"),
    path("details/<slug:slug>/", post_details, name="post_details"),
]
