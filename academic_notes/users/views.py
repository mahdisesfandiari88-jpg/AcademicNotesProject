from django.shortcuts import render, redirect
from .forms import ProfileForm
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
                return redirect("dashboard")
            return HttpResponse("Invalid email or password")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})    



def logout_view(request):
    logout(request)
    return HttpResponse("Logout Successful")

def welcome(request):
    return render(request, "welcome.html")

def dashboard(request):
    return render(request, "dashboard.html")

def profile(request):

    return render(
        request,
        "profile.html"
    )


def edit_profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )
        if form.is_valid():
            form.save()
            request.user.first_name = request.POST.get("first_name")
            request.user.last_name = request.POST.get("last_name")
            request.user.email = request.POST.get("email")
            request.user.save()
            return redirect("profile")
    else:
        form = ProfileForm(
            instance=profile
        )
    return render(
        request,
        "edit-profile.html",
        {
            "form": form
        }
    )
    form.fields["first_name"].initial = request.user.first_name
    form.fields["last_name"].initial = request.user.last_name
    form.fields["email"].initial = request.user.email