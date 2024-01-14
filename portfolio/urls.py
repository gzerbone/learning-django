from django.urls import path

from . import views



urlpatterns = [
    path('', views.home, name="portfolio-home"),
    # id dentro de <int:id> vai passar como parametro na função projects
    path('project/<int:id>/', views.projects, name="portfolio-projeto"), 
]
