from django.urls import path
from django.shortcuts import render

from . import views

urlpatterns = [
    path("", views.artikel),
    path('artikel/', views.artikel),
    path('artikel/<slug:slugInput>', views.detailArtikel),
    path('artikel/category/<str:categoryInput>', views.categoryPost)
]

