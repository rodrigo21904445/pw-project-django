from django.shortcuts import render

# Create your views here.
def index_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    
    return render(request, "users/user.html")

def login_page_view(request):
    if request.method == "POST":
        username = POST["username"]
        password = POST["password"]
        user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "users/login.html", {"message": "Invalid credentials."})

    return render(request, "users/login.html")