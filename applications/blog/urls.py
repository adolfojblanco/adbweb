from django.urls import path
from .views import posts_lists

app_name = 'blog'


urlpatterns = [
    path('', posts_lists, name='posts_list'),
]