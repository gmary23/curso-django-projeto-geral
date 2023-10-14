from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path # aqui fala para importa do todas as rotas e funções da urls do projeto


# Create your views here.
#HTTP REQUEST(cliente pede) 
# recebeu o pedido do cliente
def home(request): # foi criado essa função e colocou uma request
    return render(request, 'recipes/home.html', context={
        'name': 'Geila Martins',
    }) # direciona para a home.html que fica dentro de templates do app recipes

def contato(request): # foi criado essa função e colocou uma request
    return render(request, 'me-apague/temp.html')

def sobre(request): # foi criado essa função e colocou uma request
    return HttpResponse('SOBRE AS RECEITAS')