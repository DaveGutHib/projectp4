from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recipe
from .forms import RecipeForm

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
    