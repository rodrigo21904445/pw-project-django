from django.http.response import Http404, HttpResponse
from .models import Contacto, Quizz, Comentario
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
    contacto = Contacto.objects.get(contacto_id=contacto_id)
    form = ContactoForm(request.POST or None, instance=contacto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('soundify:contacto'))

    context = {'form': form, 'contacto_id': contacto_id, 'contacto': contacto}
    return render(request, "soundify/edita_contacto.html", context)

def apaga_contacto_view(request, contacto_id):
    Contacto.objects.get(contacto_id=contacto_id).delete()
    return HttpResponseRedirect(reverse('soundify:contacto'))

def quizz_page_view(request):
    if not request.user.is_authenticated:
            return HttpResponseRedirect("login.html")
    """
    if request.method == "POST":
        form = QuizzForm(request.POST or None)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('soundify:resultados'))

        context = {'form': form}
        return render(request, "soundify/quizz.html", context)

    form = QuizzForm(None)
    """

    anwsers = {
        'pergunta1': 'rap',
        'pergunta2': 'cleveland ohio',
        'pergunta3': 'the weeknd',
        'pergunta4': 'masked wolf',
        'pergunta5': 'astronaut in the ocean masked wolf',
        'pergunta6': 'olivia rodrigo',
        'pergunta7': 'justin bieber',
        'pergunta8': 'the weeknd',
        'pergunta9': 'bliding lights',
        'pergunta10': 'justin bieber',
    }

    if request.method == "POST":
        # cada pergunta vale dois pontos
        pontos_globais = 0

        for pergunta in anwsers:
            if(request.POST[pergunta] == anwsers[pergunta]):
                pontos_globais += 2

        return render(request, "soundify/resultados.html", {'pontos_globais': pontos_globais, 'user': request.user})

    return render(request, "soundify/quizz.html")

def comentarios_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("login.html")

    if request.method == "POST":
        new_comentario = Comentario(user=request.user, comentario=request.POST['comentario'])
        new_comentario.save()

    return render(request, "soundify/comentarios.html")

def section(request, num):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("login.html")
    
    pages = [
        "index.html",
        "search.html",
        "quizz.html",
        "comentarios.html",
        "contactos.html",
        "login.html",
        "logout.html",
        "register.html",
    ]

    pages_dict = {
        "index.html": index_page_view(request),
        "search.html": search_page_view(request),
        "quizz.html": quizz_page_view(request),
        "comentarios.html": comentarios_page_view(request),
        "contactos.html": contacto_page_view(request),
        "login.html": login_page_view(request),
        "logout.html": logout_page_view(request),
        "register.html": register_page_view(request),
    }

    if 1 <= num <= 8:
        key = pages[num -1]
        return HttpResponse(pages_dict[key])        
    else:
        raise Http404("No such section")