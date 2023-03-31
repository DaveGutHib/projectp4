from django.views.generic import CreateView, TemplateView, ListView

#  Checks user in logged in before allowing recipe creation
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from .forms import RecipeForm

class Recipes(ListView):
    """ View list of recipes """
    template_name = 'recipe/recipes.html'
    model = Recipe
    context_object_name = 'recipes'

class Index(TemplateView):
    template_name = 'recipe/index.html'

class AddRecipe(LoginRequiredMixin, CreateView):
    """ Add recipe view """
    template_name = 'recipe/add_recipe.html'
    model = Recipe
    form_class = RecipeForm
    success_url = '/recipe/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)
    