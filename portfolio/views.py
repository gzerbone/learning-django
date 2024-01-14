from django.shortcuts import render

from utils.portfolio.factory import make_portfolio


def home(request):
    return render(request, 'portfolio/pages/home.html', context={
        'portfolios': [make_portfolio() for var in range(4)], 
    })


def projects(request, id):
    return render(request, 'portfolio/pages/projects_view.html', context={
        'portfolio': make_portfolio(),
        'is_detail_page': True, #Se a pagina for a pagina de um projeto o botão de "ver mais não vai existir"
        })
