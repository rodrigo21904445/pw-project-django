from os import name
from django.shortcuts import render
from . import views
from django.urls import path

app_name = "soundify"

urlpatterns = [
    path('', views.index_page_view, name='index'),
    path('index.html', views.index_page_view, name="index"),
    path('search.html', views.search_page_view, name='search'), 
    path('register.html', views.register_page_view, name="register"),
    path('feedback.html', views.feedback_page_view, name="feedback"),
    path('sections/login.html', views.login_page_view, name='login'),
    path('login.html', views.login_page_view, name='login'),
    path('logout', views.logout_page_view, name='logout'),
    path('user.html', views.user_page_view, name='user'),
    path('contacto.html', views.contacto_page_view, name='contacto'),
    path('novo_contacto.html', views.novo_contacto_view, name='novo'),
    path('edita_contacto.html/<int:contacto_id>', views.edita_contacto_view, name='edita'),
    path('apaga/<int:contacto_id>', views.apaga_contacto_view, name='apaga'),
    path('quizz.html', views.quizz_page_view, name='quizz'),
    path('comentarios.html', views.comentarios_page_view, name='comentarios'),
    path('sections/<int:num>', views.section, name='section'),
]
