from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("izin-amatir-radio/", views.amatirRadio),
    path("izin-stasiun-radio/", views.stasiunRadio),
    path("ujian-negara-amatir/", views.ujianNegara),
    path("layanan-pengaduan/", views.layananPengaduan),
    path('SERENA/', views.serena),
    path('SIRANI/', views.sirani)
]