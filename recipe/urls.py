from django.urls import path
from .views import Index, AddRecipe, Recipes

urlpatterns = [
    path('', AddRecipe.as_view(), name='add_recipe'),
    path('', Index.as_view(), name='recipe')
    
]