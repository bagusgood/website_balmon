from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Banner, Post


def index(request):
    banner = Banner.objects.all()
    post = Post.objects.all()
    context = {
        "headline": "Direktorat Jenderal Infrastruktur Digital",
        "nav": [
            ["/", 'Beranda'],
            ['/profiles', 'Profiles'],
            ['/regulasi', 'Regulasi'],
            ['/blog', 'Blog'],
        ],
        "gambar": banner,
        "postingan": post
    }
    return render(request, "index.html", context)

def test(request, angka):
    return HttpResponse("<h1>Hallo</h1>")

# def struktur(request):
#     return render(request, "struktur.html")

# def tugas(request):
#     return render(request, "tugas.html")

# def visiMisi(request):
#     return render(request, "visiMisi.html")

# def kepalaBalmon(request):
#     return render(request, "kepalaBalmon.html")

# def contact(request):
#     return render(request, "contact.html")