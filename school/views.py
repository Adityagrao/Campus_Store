from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_user_model
# Create your views here.
from django.shortcuts import render
from .forms import UserLoginForm


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
    return render(request, "school/login.html", {"form": form})


def logout_view(request):
    return render(request, "school/logout.html", {})


def parent_user(request):
    return render(request, "parent_user/index.html", {})


def school_admin(request):
    return render(request, "school_admin/index.html", {})


def super_admin(request):
    return render(request, "super_admin/index.html", {})
