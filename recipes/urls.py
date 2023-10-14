from django.urls import path
#from django.contrib import admin
from recipes.views import home, contato, sobre

urlpatterns = [
    path('', home),  # Home
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato),  # /contato/
]