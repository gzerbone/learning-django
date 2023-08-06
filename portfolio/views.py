from django.shortcuts import render


def home(request):
    return render(request, 'portfolio/pages/home.html')


def projects(request, id):
    return render(request, 'portfolio/pages/projects_view.html')
