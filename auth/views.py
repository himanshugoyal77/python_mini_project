from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "auth/index.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        rpassword = request.POST['rpassword']
        print("User is authenticated")
        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        messages.success(request, "Your account has been successfully created")

        return redirect("home")
    return render(request, "auth/signin.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print("User is authenticated")
        if user is not None:
            login(request, user)
            print("User is authenticated")
            messages.success(request, "You are now logged in")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("signin")
    return render(request, "auth/signup.html")


def signout(request):
    pass


def login_page(request):
    return render(request, "auth/login.html")


def register_page(request):
    return render(request, "auth/register.html")