from os import name
from django.shortcuts import render
from . import views
from django.urls import path

app_name = "users"

urlpatterns = [
    path('', views.index_page_view, name='index'),
    path('login', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),
]
