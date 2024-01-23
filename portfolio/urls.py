from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name="home"),
    # id dentro de <int:id> vai passar como parametro na função projects
    path('project/<int:id>/', views.projects, name="projeto"), 
]
