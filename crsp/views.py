from django.shortcuts import render, redirect
import pandas as pd
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from crsp.models import Recipes, Rates


# Create your views here.
def index(request):
    print("index requested")
    data1 = Recipes.objects.all().order_by('-id')[0:1]
    data2 = Recipes.objects.all().order_by('-id')[1:2]
    data3 = Recipes.objects.all().order_by('-id')[2:3]
    data4 = Recipes.objects.all().order_by('-id')[3:4]
    data5 = Recipes.objects.all().order_by('-id')[4:5]
    data6 = Recipes.objects.all().order_by('-id')[5:6]

    data1_id = list(data1.values("id"))[0]['id']
    data2_id = list(data2.values("id"))[0]['id']
    data3_id = list(data3.values("id"))[0]['id']
    data4_id = list(data4.values("id"))[0]['id']
    data5_id = list(data5.values("id"))[0]['id']
    data6_id = list(data6.values("id"))[0]['id']

    try:
        recipe_rate1 = pd.DataFrame(list(Rates.objects.filter(recipe_id=data1_id).values("rate")))['rate'].mean()
    except:
        recipe_rate1 = None
    
    try:
        recipe_rate2 = pd.DataFrame(list(Rates.objects.filter(recipe_id=data2_id).values("rate")))['rate'].mean()
    except:
        recipe_rate2 = None
    
    try:
        recipe_rate3 = pd.DataFrame(list(Rates.objects.filter(recipe_id=data3_id).values("rate")))['rate'].mean()
    except:
        recipe_rate3 = None

    try:
        recipe_rate4 = pd.DataFrame(list(Rates.objects.filter(recipe_id=data4_id).values("rate")))['rate'].mean()
    except:
        recipe_rate4 = None

    try:
        recipe_rate5 = pd.DataFrame(list(Rates.objects.filter(recipe_id=data5_id).values("rate")))['rate'].mean()
    except:
        recipe_rate5 = None
    
    try:
        recipe_rate6 = pd.DataFrame(list(Rates.objects.filter(recipe_id=data6_id).values("rate")))['rate'].mean()
    except:
        recipe_rate6 = None

    return render(request, 'crsp/index.html', {"data1": data1, "data2": data2, "data3": data3, "data4": data4, "data5": data5, "data6": data6, "recipe_rate1":recipe_rate1, "recipe_rate2":recipe_rate2, "recipe_rate3":recipe_rate3, "recipe_rate4":recipe_rate4, "recipe_rate5":recipe_rate5, "recipe_rate6":recipe_rate6})

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
    data = Recipes.objects.all().filter(user_id=request.user.id)
    print("recipes requested")
    return render(request, 'crsp/recipes.html', {"data": data})

def recipe(request, objectid):
    data = Recipes.objects.get(id=objectid)
    try:
        recipe_rate = pd.DataFrame(list(Rates.objects.filter(recipe_id=objectid).values("rate")))['rate'].mean()
    except:
        recipe_rate = None

    creator = User.objects.get(id=data.user_id)
    
    try:
        is_rated = Rates.objects.filter(recipe_id=objectid, user_id=request.user.id)
    except:
        is_rated = False
    finally:
        if data.user_id == request.user.id:
            is_rated = True
    
    return render(request, 'crsp/recipe.html', {"data": data, "creator": creator, "is_rated": is_rated, "recipe_rate": recipe_rate})

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
        return redirect("recipes")
    
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

def search(request):
    search_key = request.POST['search']
    data = Recipes.objects.filter(title__icontains=f"{search_key}")
    return render(request, "crsp/search.html", {"data": data})

def rate(request):
    if request.method == "POST":
        rate = request.POST['stars']
        recipe_id = request.META['HTTP_REFERER'].split("/")[-1]
        data = {
            "rate": rate,
            "user_id": request.user.id,
            "recipe_id": recipe_id
        }
        recipe = Rates(**data)
        recipe.save()

        return redirect("/recipe/"+recipe_id)