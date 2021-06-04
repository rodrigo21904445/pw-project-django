from os import name
from django.shortcuts import render
from . import views
from django.urls import path

app_name = "soundify"

urlpatterns = [
    path('', views.index_page_view, name='index'),
    path('index.html', views.index_page_view, name="index"),
    path('search.html', views.search_page_view, name='search'), 
    path('login.html', views.login_page_view, name="login"),
    path('register.html', views.register_page_view, name="register"),
    path('feedback.html', views.feedback_page_view, name="feedback"),
]
