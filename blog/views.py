from django.shortcuts import render
from .models import BlogPost
import random


def blog_view(request):
    posts = BlogPost.objects.all()
    context = {"posts": posts}
    return render(request, "blog/blog.html", context)


def blog_detail(request, id):
    post = BlogPost.objects.get(id=id)
    more_posts = random.sample(list(BlogPost.objects.exclude(id=id)), 3)
    context = {
        "post": post,
        "more_posts": more_posts,
    }
    return render(request, "blog/blog-detail.html", context)
