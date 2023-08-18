from django.shortcuts import render
from .models import BlogPost

def blog_view(request):
    posts = BlogPost.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "blog/blog.html", context)

def blog_detail(request, id):
    post = BlogPost.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, "blog/blog-detail.html", context)