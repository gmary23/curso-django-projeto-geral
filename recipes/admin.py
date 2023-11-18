from django.contrib import admin

from .models import Category, Recipe  # Importou a classe Category do models.py


class CategoryAdmin(
    admin.ModelAdmin
):  # criação de classe para registrar no admin que herda
    ...


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...


admin.site.register(
    Category, CategoryAdmin
)  # Category --> model e CategoryAdmin --> criado para herdar de models
