from django.shortcuts import render


def home(request):
    return render(request, 'portfolio/pages/home.html')


def users(request):
    return render(request, 'portfolio/pages/users.html')
