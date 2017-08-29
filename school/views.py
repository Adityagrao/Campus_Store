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
