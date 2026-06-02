from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.struktur),
    path('struktur-organisasi/', views.struktur),
    path("tugas-fungsi/", views.tugas),
    path('visi-misi/', views.visiMisi),
    path('struktur-organisasi/kasubag', views.kasubag),
    path('struktur-organisasi/monev', views.monev),
    path('struktur-organisasi/penertiban', views.penertiban),
    path('struktur-organisasi/pemeliharaan', views.pemeliharaan),
]