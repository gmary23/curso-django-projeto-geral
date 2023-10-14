from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path # aqui fala para importa do todas as rotas e funções da urls do projeto

# Create your views here.
#HTTP REQUEST(cliente pede) 
# recebeu o pedido do cliente
def home(request): # foi criado essa função e colocou uma request
    return HttpResponse('Deu certo a primeira home do app recipes ....Show de bola') # foi respondido ao cliente

def contato(request): # foi criado essa função e colocou uma request
    return HttpResponse('CONTATO GEILA')

def sobre(request): # foi criado essa função e colocou uma request
    return HttpResponse('SOBRE AS RECEITAS')