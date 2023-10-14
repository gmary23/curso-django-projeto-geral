"""
URL configuration for projeto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

#HTTP REQUEST(cliente pede) 
# recebeu o pedido do cliente
def home(request): # foi criado essa função e colocou uma request
    return HttpResponse('HOME') # foi respondido ao cliente

def sobre(request): # foi criado essa função e colocou uma request
    return HttpResponse('SOBRE')

def contato(request): # foi criado essa função e colocou uma request
    return HttpResponse('CONTATO')

urlpatterns = [
    path('admin/', admin.site.urls),
    # aqui o cliente pediu 
    path('', home), # esse vazio entre aspas significa que vai pra página principal.
    path('sobre/', sobre),#  uma path recebe uma ROTA (caminho) e uma FUNÇÃO.
    path('contato/', contato),

]
