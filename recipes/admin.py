from django.contrib import admin

from .models import Category  # Importou a classe Category do models.py


class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)
