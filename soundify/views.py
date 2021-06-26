from .models import Contacto
from .forms import ContactoForm
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def index_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("login.html")
    
    return render(request, "soundify/index.html")

def search_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("login.html")
    
    return render(request, "soundify/search.html")

def register_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("login.html")
    
    return render(request, 'soundify/register.html')

def feedback_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("login.html")
    
    return render(request, 'soundify/feedback.html')
"""
def index_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("login.html")
    
    #return render(request, "soundify/user.html")
    return render(request, "soundify/index.html")
"""
def user_page_view(request):
    return render(request, "soundify/user.html")

def login_page_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect("user.html")

        else:
            return render(request, "soundify/login.html", {"message": "Invalid credentials."})

    return render(request, "soundify/login.html")

def logout_page_view(request):
    logout(request)
    return render(request, "soundify/login.html", {"message": "Logged out."})

def contacto_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("login.html")

    context = {'contactos': Contacto.objects.all()}
    return render(request, 'soundify/contacto.html', context)

def novo_contacto_view(request):
    form = ContactoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('soundify:contacto'))
    context = {'form': form}
    return render(request, "soundify/novo_contacto.html", context)

def edita_contacto_view(request, contacto_id):
    contacto = Contacto.objects.get(id=contacto_id)
    form = ContactoForm(request.POST or None, instance=contacto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('soundify:contacto'))

    context = {'form': form, 'contacto_id': contacto_id}
    return render(request, 'soundify/edita_contacto.html', context)

def apaga_contacto_view(request, contacto_id):
    Contacto.objects.get(id=contacto_id).delete()
    return HttpResponseRedirect(reverse('soundify:contacto'))