from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe


def home(request):
    recipes = Recipe.objects.all().order_by("-id")  # aplicativo
    return render(
        request,
        "recipes/pages/home.html",
        context={
            "recipes": recipes,  # nome das receitas que tem cadastradas
        },
    )


def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category__id).order_by(
        "-id"
    )  # aplicativo
    return render(
        request,
        "recipes/pages/home.html",
        context={
            "recipes": recipes,  # nome das receitas que tem cadastradas
        },
    )


def recipe(request, id):
    return render(
        request,
        "recipes/pages/recipe-view.html",
        context={
            "recipe": make_recipe(),
            "is_detail_page": True,
        },
    )
