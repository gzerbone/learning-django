from django.shortcuts import render


def home(request):
    return render(request, 'portfolio/pages/home.html')


def users(request, id):
    return render(request, 'portfolio/pages/users.html')
