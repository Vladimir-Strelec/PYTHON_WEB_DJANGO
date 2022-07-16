from django.shortcuts import render, redirect

from Recipes.web.forms import CreatePicaForm, EditPicaForm, DeletePicaForm
from Recipes.web.models import Recipe


# def get_recipes():
#     recipes = Recipe.objects.all()
#     if recipes:
#         return recipes[0]
#     return None
def action_form_create(request):
    if request.method == 'POST':
        form = CreatePicaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = CreatePicaForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def action_edit_form(request, current_form, current_redirect, current_template, instance):
    if request.method == "POST":
        form = current_form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(current_redirect)
    form = current_form(instance=instance)
    context = {
        'form': form,
        'pk': instance,
    }
    return render(request, current_template, context)


def home_page(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,

    }
    return render(request, 'index.html', context)


def create_recipe(request):
    return action_form_create(request)


def edit_recipe(request, pk):
    return action_edit_form(request, EditPicaForm, 'index', 'edit.html', Recipe.objects.get(pk=pk))


def delete_recipe(request, pk):
    return action_edit_form(request, DeletePicaForm, 'index', 'delete.html', Recipe.objects.get(pk=pk))


def recipe_details(request, pk):
    ingredients = Recipe.objects.get(pk=pk).ingredients.split(', ')
    context = {
        'recipes': Recipe.objects.get(pk=pk),
        'ingredients': ingredients,
    }
    return render(request, 'details.html', context)
