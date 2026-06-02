from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.undang_undang),
    path('undang-undang/', views.undang_undang),
    path("peraturan-pemerintah/", views.peraturan_pemerintah)
]