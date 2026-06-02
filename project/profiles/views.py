from django.shortcuts import render

def struktur(request):
    context = {
        "headline": "Profiles",
        "title": ["Struktur Organisasi", "Tugas & Fungsi", "Profiles"],
        "anggota": [
            ["Hendra Oktobian An Fasa", "Nama Tim"],
            ["Hendra Oktobian An Fasa", "Nama Tim"],
            ["Hendra Oktobian An Fasa", "Nama Tim"],
            ["Hendra Oktobian An Fasa", "Nama Tim"],
        ],
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
        "app_css": "blog/css/style.css"
    }
    return render(request, "profiles/struktur.html", context)

def kasubag(request):
    context = {
        "headline": "Profiles",
        "title": ["Struktur Organisasi", "Tugas & Fungsi", "Profiles"],
        "anggota": [
            ["Hendra Oktobian An Fasa", "Boss Besar"],
            ["Hendra Oktobian An Fasa", "Boss Besar"],
            ["Hendra Oktobian An Fasa", "Boss Besar"],
            ["Hendra Oktobian An Fasa", "Boss Besar"],
        ],
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
        "app_css": "blog/css/style.css"
    }
    return render(request, "profiles/kasubag.html", context)

def monev(request):
    context = {
        "headline": "Profiles",
        "title": ["Struktur Organisasi", "Tugas & Fungsi", "Profiles"],
        "anggota": [
            ["Hendra Oktobian An Fasa", "Boss Besar"],
            ["Hendra Oktobian An Fasa", "Boss Besar"],
            ["Hendra Oktobian An Fasa", "Boss Besar"],
            ["Hendra Oktobian An Fasa", "Boss Besar"],
        ],
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
        "app_css": "blog/css/style.css"
    }
    return render(request, "profiles/monev.html", context)

def penertiban(request):
    context = {
        "headline": "Profiles",
        "title": ["Struktur Organisasi", "Tugas & Fungsi", "Profiles"],
        "anggota": [
            ["Hendra Oktobian An Fasa", "Boss Besar"],
            ["Hendra Oktobian An Fasa", "Boss Besar"],
            ["Hendra Oktobian An Fasa", "Boss Besar"],
            ["Hendra Oktobian An Fasa", "Boss Besar"],
        ],
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
        "app_css": "blog/css/style.css"
    }
    return render(request, "profiles/penertiban.html", context)

def pemeliharaan(request):
    context = {
        "headline": "Profiles",
        "title": ["Struktur Organisasi", "Tugas & Fungsi", "Profiles"],
        "anggota": [
            ["Hendra Oktobian An Fasa", "Pegawai"],
            ["Hendra Oktobian An Fasa", "Pegawai"],
            ["Hendra Oktobian An Fasa", "Pegawai"],
            ["Hendra Oktobian An Fasa", "Pegawai"],
        ],
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
        "app_css": "blog/css/style.css"
    }
    return render(request, "profiles/pemeliharaan.html", context)\
        
def tugas(request):
    context = {
        "headline": "Profiles",
        "title": ["Struktur Organisasi", "Tugas & Fungsi", "Profiles"],
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
        "app_css": "blog/css/style.css"
    }
    return render(request, "profiles/tugas.html", context)

def visiMisi(request):
    context = {
        "headline": "Profiles",
        "title": ["Struktur Organisasi", "Tugas & Fungsi", "Profiles", "Visi & Misi"],
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
        "app_css": "blog/css/style.css"
    }
    return render(request, "profiles/visimisi.html", context)