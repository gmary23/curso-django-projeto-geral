from django.shortcuts import render


# Create your views here.
# HTTP REQUEST(cliente pede)
# recebeu o pedido do cliente
def home(request):  # foi criado essa função e colocou uma request
    return render(
        request,
        "recipes/pages/home.html",
        context={
            "name": "Geila Martins",
        },
    )  # direciona para a home.html que fica dentro de templates do app recipes


def recipe(request, id):
    return render(request, "recipes/pages/home.html", context={"name": "Geila Azevedo"})
