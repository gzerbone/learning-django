from django.shortcuts import get_object_or_404, render

from portfolio.models import Category, Portfolio
from utils.portfolio.factory import make_portfolio

# conectar models e templates

def home(request):
    cards = Portfolio.objects.filter(is_published=True).order_by('-id')
    return render(request, 'portfolio/pages/home.html', context={
        'portfolios':cards, 
    })

def category(request, category_id):
    category_cards = Portfolio.objects.filter(
        category__id = category_id, is_published=True
        )
    # função get_object_or_404 para obter a categoria específica com base no category_id. 
    categoria = get_object_or_404(Category, id=category_id)
    return render(request, 'portfolio/pages/category.html', context={
        'portfolios':category_cards,
        'category_title': categoria.name
    })

def projects(request, id):
    return render(request, 'portfolio/pages/projects_view.html', context={
        'portfolio': make_portfolio(),
        'is_detail_page': True, #Se a pagina for a pagina de um projeto o botão de "ver mais não vai existir"
        })
