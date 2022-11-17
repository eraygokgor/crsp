from django.shortcuts import render, redirect
import psycopg2
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# Create your views here.
def index(request):
    print("index requested")
    return render(request, 'crsp/index.html')

def signup(request):
    print("signup requested")
    return render(request, 'crsp/signup.html')

def login(request):
    print("login requested")
    return render(request, 'crsp/login.html')

def profile(request):
    print("profile requested")
    return render(request, 'crsp/profile.html')

def register_user(request):
    print("register_user requested")
    if request.method == 'POST':
        username = request.POST.get("inputEmail")
        email = request.POST.get("inputEmail")
        password = request.POST.get("inputPassword")
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = request.POST.get("inputName")
        user.last_name = request.POST.get("inputLastName")
        user.save()
        return redirect("/")


def logout(request):
    print("logout requested")
    auth_logout(request)
    return redirect("/")


def signin(request):
    print("signin requested")
    if request.method == 'POST':
        print("POST")
        try:
            username = request.POST["inputEmail"]
            password = request.POST["inputPassword"]
            user = authenticate(request, username=username, password=password)
            auth_login(request, user)
            if user is not None:
                print(request.user.is_authenticated)
                name = user.first_name
                lastname = user.last_name
                return render(request, 'crsp/profile.html', {'name': user.first_name, 'lastname': user.last_name,})
            else:
                return render(request, 'crsp/login.html', {'auth': 0})
        except:
            return render(request, 'crsp/login.html', {'auth': 0})
    if request.method == 'GET' and request.user.is_authenticated:
        print("signin GET req")
        user = request.user
        return render(request, 'crsp/profile.html', {'name': user.first_name, 'lastname': user.last_name,})