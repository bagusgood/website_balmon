from django.shortcuts import render
from .models import Banner, Post

# Create your views here.

def artikel(request):
    gambar = Banner.objects.all()
    posts = Post.objects.all()
    context = {
        "headline": "Blog",
        "title": ["Artikel"],
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
        "banner": gambar,
        "postingan": posts
    }
    return render(request, "blog/artikel.html", context)

def detailArtikel(request, slugInput):
    gambar = Banner.objects.all()
    posts = Post.objects.get(slug = slugInput)
    context = {
        "headline": "Blog",
        "title": ["Artikel"],
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
        "banner": gambar,
        "postingan": posts
    }
    return render(request, "blog/detailPost.html", context)

def categoryPost(request, categoryInput):
    gambar = Banner.objects.all()
    posts = Post.objects.filter(category=categoryInput)
    context = {
        "headline": "Blog",
        "title": ["Artikel"],
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
        "banner": gambar,
        "postingan": posts
    }
    return render(request, "blog/categoryPost.html", context)