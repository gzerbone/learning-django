from django.urls import path
from portfolio.views import home, users

urlpatterns = [
    path('', home),
    path('users/', users),
]
