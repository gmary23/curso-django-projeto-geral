from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views
from recipes.models import Category, Recipe, User


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
    
    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(  # verifica se tem um texto
            '<h1>No recipes found here</h1>',
            response.content.decode('utf-8')
        )
<<<<<<< HEAD
    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
=======
    def teste_recipe_home_template_loads_recipes(self): # testa se o templete da home carrega as receitas
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )

        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title = 'Recipe Title',
            description = 'Recipe Description',
            slug = 'recipe-slug',
            preparation_time = 10,
            preparation_time_unit ='Minutos', 
            servings = 5,
            servings_unit ='Porções', 
            preparation_steps ='Recipe Prepatation Steps', 
            preparation_steps_is_html=False
            is_published=True
        )
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']

        self.assertIn('Recipe Title', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('5 Porções', content)
        self.assertEqual(len(response_context_recipes), 1)
        ...

    def teste_recipe_home_shows_no_recipes_found_if_no_recipes(self):
>>>>>>> f6de8517122ed461d25cad65b9abf2e823f8f270
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(  # verifica se tem um texto
            '<h1>No recipes found here</h1>',
            response.content.decode('utf-8')
        )