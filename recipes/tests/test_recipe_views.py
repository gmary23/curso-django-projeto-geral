from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views


class RecipeViewsTest(TestCase):
    def test_recipe_home_views_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)
    
    # get é o que o cliente faz quando acessa o servidor /
    # por padrão o navegador faz get

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        # Verifica se o código de status da resposta é igual a 200  
        # esse 200 significa que a requisição foi bem sucedida
        self.assertEqual(response.status_code, 200) 
    
    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        # Verifica se o código de status da resposta é igual a 200  
        # esse 200 significa que a requisição foi bem sucedida
        self.assertTemplateUsed(response, 'recipes/pages/home.html') 
    
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h1>No recipes found here 🥲</h1>',
            response.content.decode('utf-8')
        )
