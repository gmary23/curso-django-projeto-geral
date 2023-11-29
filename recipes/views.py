from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe
from django.shortcuts import get_list_or_404, render


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
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by("-id")
    )

    return render(
        request,
        "recipes/pages/category.html",
        context={
            "recipes": recipes,  # nome das receitas que tem cadastradas
            "title": f"{recipes[0].category.name} - Category |",
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
