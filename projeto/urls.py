from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),# recebe do arquivo e a url que vai incluir
   # path('recipes/', include('recipes.urls')),
]
