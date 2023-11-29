from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe
from django.http import Http404


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")  # aplicativo
    return render(
        request,
        "recipes/pages/home.html",
        context={
            "recipes": recipes,  # nome das receitas que tem cadastradas
        },
    )


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by("-id")
    if not recipes:
        raise Http404("Essa página não existe")

    return render(
        request,
        "recipes/pages/category.html",
        context={
            "recipes": recipes,  # nome das receitas que tem cadastradas
            "title": f"{recipes.first().category.name} - Category |",
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
