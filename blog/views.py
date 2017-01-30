from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def home_page(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, "blog/index.html", context)


def post_page(request, id):
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }

    return render(request, "blog/post.html", context)