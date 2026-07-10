from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(
                request,
                email=email,
                password=password
            )
            if user is not None:
                login(request, user)
                return HttpResponse("Login Successful")
            return HttpResponse("Invalid email or password")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})    


def logout_view(request):
    logout(request)
    return HttpResponse("Logout Successful")

def welcome(request):
    return render(request, "welcome.html")