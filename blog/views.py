from django.shortcuts import render
from .models import Blog

def blog_view(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "blog/blog.html", context)