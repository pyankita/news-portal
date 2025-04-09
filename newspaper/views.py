from django.shortcuts import render
from newspaper.models import Post
from django.views.generic import ListView

class HomeView(ListView):
    model=Post
    template_name="newsportal/home.html"
    context_object_name="posts"
    queryset=Post.objects.filter(
        published_at__isnull=False,status="active"

    ).orderby("-published_at")[:4]

