from django.shortcuts import render

# Create your views here.
def index_page_view(request):
    return render(request, "soundify/index.html")

def search_page_view(request):
    return render(request, "soundify/search.html")

def login_page_view(request):
    return render(request, 'soundify/login.html')

def register_page_view(request):
    return render(request, 'soundify/register.html')

def feedback_page_view(request):
    return render(request, 'soundify/feedback.html')

