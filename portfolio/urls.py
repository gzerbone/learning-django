from django.urls import path

from . import views

app_name = 'portfolio'

# name="projeto", name="home" e name="category" são 
# os nomes das URLs que serão usadas para identificar a View

urlpatterns = [
    path('', views.home, name="home"),
    # id dentro de <int:id> vai passar como parametro na função projects
    path('project/<int:id>/', views.projects, name="projeto"), 
    path('project/category/<int:category_id>/', views.category, name="category"), 
]
