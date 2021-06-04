from django.shortcuts import render
from . import views
from django.urls import path

app_name = "soundify"

urlpatterns = [
    path('', views.index_page_view, name='index')
]
