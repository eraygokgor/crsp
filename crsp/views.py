from django.shortcuts import render, redirect
import psycopg2
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from crsp.models import Recipes


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

def add(request):
    print("add requested")
    return render(request, 'crsp/add.html')

def recipes(request):
    print("add requested")
    return render(request, 'crsp/recipes.html')

def settings(request):
    print("settings requested")
    if request.user.is_authenticated:
        user = request.user
        return render(request, "crsp/settings.html", {"email": user.email, "first_name": user.first_name, "last_name": user.last_name})
def add_recipe(request):
    if request.method == "GET":
        return render(request, "clickandrent/add.html")
    if request.method == "POST":
        # Data
        title = request.POST['inputTitle']
        beans = request.POST['inputBeans']
        roast = request.POST['inputRoast']
        grinder = request.POST['inputGrinder']
        click = request.POST['inputGrinderClick']
        method = request.POST['inputMethod']
        blooming = request.POST['inputBlooming']
        duration = request.POST['inputDuration']
        ratio = request.POST['inputRatio']
        descripton = request.POST['inputDescription']

        data = {
            "user_id": request.user.id,
            "title": title,
            "beans": beans,
            "roast": roast,
            "grinder": grinder,
            "click": click,
            "method": method,
            "blooming": blooming,
            "duration": duration,
            "ratio": ratio,
            "method": method,
            "descripton": descripton,
        }

        recipe = Recipes(**data)
        recipe.save()
        print("recipe saved")
        return redirect("add")
    
def register_user(request):
    print("register_user requested")
    if request.method == 'POST':
        if User.objects.filter(email=request.POST.get("inputEmail")).exists():
            return render(request, "crsp/signup.html", {'existing': 1})
        else:
            username = request.POST.get("inputEmail")
            email = request.POST.get("inputEmail")
            password = request.POST.get("inputPassword")
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = request.POST.get("inputName")
            user.last_name = request.POST.get("inputLastName")
            user.save()
            return render(request, "crsp/signup.html", {'saved': 1})
            # return redirect("/")


def logout(request):
    print("logout requested")
    auth_logout(request)
    return redirect("/")

def changes(request):
    print("changes requested")
    if request.method == "POST":
        try:
            new_password = request.POST["inputPassword"]
            first_name = request.POST["firstName"]
            last_name = request.POST["lastName"]
            user = request.user
            if new_password != '':
                print(new_password)
                user.set_password(new_password)
            if first_name != '':
                print(first_name)
                user.first_name = first_name
            if last_name != '':
                print(last_name)
                user.last_name = last_name
            user.save()
            return redirect("/")
        except:
            print(e)
            return render(request, 'crsp/index.html')

def delete(request):
    print("delete requested")
    if request.user.is_authenticated:
        user = request.user
        request.user.delete()
        auth_logout(request)
        return redirect("/")

def signin(request):
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
                #return render(request, 'crsp/index.html')
                return redirect("/")
            else:
                return render(request, 'crsp/login.html', {'auth': 0})
        except Exception as e:
            return render(request, 'crsp/login.html', {'auth': 0})
    if request.method == 'GET' and request.user.is_authenticated:
        user = request.user
        # return render(request, 'crsp/index.html')
        return redirect("/")