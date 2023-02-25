from django.urls import path
from recipes.views import about, home, users

urlpatterns = [
    path('', home),
    path('about/', about),
    path('users/', users),
]
