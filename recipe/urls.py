from django.urls import path
from .views import Index, AddRecipe, Recipes, RecipeDetail

urlpatterns = [
    path("", AddRecipe.as_view(), name="add_recipe"),
    path("", Index.as_view(), name="recipe"),
    path("recipes/", Recipes.as_view(), name="recipes"),
    path("<slug:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
]
