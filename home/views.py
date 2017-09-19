from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def parent_login(request):
    return render(request, 'parent_user/pages-login.html')

def parent_register(request):
    return render(request, 'parent_user/pages-register.html')