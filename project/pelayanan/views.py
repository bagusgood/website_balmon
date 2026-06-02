from django.shortcuts import render

# Create your views here.
def amatirRadio(request):
    context = {
        "headline": "Pelayanan",
        "title": ["Izin Amatir Radio & IKRAP", "Tugas & Fungsi", "Profiles"],
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
        "app_css": "blog/css/style.css"
    }
    return render(request, "pelayanan/izin-amatir-radio.html", context)

def stasiunRadio(request):
    context = {
        "headline": "Pelayanan",
        "title": ["Izin Amatir Radio & IKRAP", "Izin Stasiun Radio", "Profiles"],
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
        "app_css": "blog/css/style.css"
    }
    return render(request, "pelayanan/izin-stasiun.html", context)

def ujianNegara(request):
    context = {
        "headline": "Pelayanan",
        "title": ["Izin Amatir Radio & IKRAP", "Izin Stasiun Radio", "Ujian Negara Amatir Radio"],
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
        "app_css": "blog/css/style.css"
    }
    return render(request, "pelayanan/ujian-negara-amatir.html", context)

def layananPengaduan(request):
    context = {
        "headline": "Pelayanan",
        "title": ["Izin Amatir Radio & IKRAP", "Izin Stasiun Radio", "Ujian Negara Amatir Radio", "Layanan Pengaduan Masyarakat"],
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
        "app_css": "blog/css/style.css"
    }
    return render(request, "pelayanan/layanan-pengaduan.html", context)

def serena(request):
    context = {
        "headline": "Serena",
        "title": ["Izin Amatir Radio & IKRAP", "Izin Stasiun Radio", "Ujian Negara Amatir Radio", "Layanan Pengaduan Masyarakat", "Sertifikasi Operator Radio Untuk Pelayaran Rakyat (SERENA)"],
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
        "app_css": "blog/css/style.css"
    }
    return render(request, "pelayanan/serena.html", context)

def sirani(request):
    context = {
        "headline": "Sirani",
        "title": ["Izin Amatir Radio & IKRAP", "Izin Stasiun Radio", "Ujian Negara Amatir Radio", "Layanan Pengaduan Masyarakat", "Sertifikasi Operator Radio Untuk Pelayaran Rakyat (SERENA)", "Sertifikasi Perangkat Telekomunikasi (SIRANI)"],
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
        "app_css": "blog/css/style.css"
    }
    return render(request, "pelayanan/sirani.html", context)