from django.views.generic import (CreateView,TemplateView,ListView,DetailView,DeleteView)

#  Checks user in logged in before allowing recipe creation
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from .forms import RecipeForm


class Recipes(ListView):
    """View list of recipes"""

    template_name = "recipe/recipes.html"
    model = Recipe
    context_object_name = "recipes"


class RecipeDetail(DetailView):
    """View a recipes details"""

    template_name = "recipe/recipes.html"
    model = Recipe
    context_object_name = "recipe"


class Index(TemplateView):
    """ View recipe template"""
    template_name = "recipe/index.html"


class AddRecipe(LoginRequiredMixin, CreateView):
    """Add recipe view"""

    template_name = "recipe/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipe/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)

class DeleteRecipe(DeleteView):
    """Delete uploaded recipe"""
    model = Recipe
    success_url = '/recipes/'
