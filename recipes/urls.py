from django.urls import path
from recipes.views import home, users

urlpatterns = [
    path('', home),
    path('users/', users),
]
