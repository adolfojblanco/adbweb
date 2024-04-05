from django.shortcuts import render

from .models import Post

# Create your views here.


def posts_lists(request):
    posts = Post.objects.all()
    return render(request, "blog/list_post.html", {"posts": posts})


def post_details(request, slug):
    post = Post.objects.filter(slug=slug)[0]
    return render(request, "blog/datail_post.html", {"post": post})
