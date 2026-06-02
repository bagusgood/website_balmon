from django.shortcuts import render

def undang_undang(request):
    context = {
        "headline": "Regulasi",
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
    }
    return render(request, "regulasi/undang.html", context)

def peraturan_pemerintah(request):
    context = {
        "headline": "Regulasi",
        "nav": [
            ["/", "Home"],
            ["/blog", 'Blog'],
        ],
    }
    return render(request, "regulasi/pemerintah.html", context)