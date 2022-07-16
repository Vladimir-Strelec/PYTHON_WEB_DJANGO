from django.shortcuts import render, redirect

from Exam_preparation.web.forms import CreateProfileForm, CreateExpenseForm, DeleteProfile, DeleteExpense
from Exam_preparation.web.models import Profile, Expense
from django.views import generic as views


def get_profile():
    current_profile = Profile.objects.all()
    if current_profile:
        return current_profile[0]
    return None


def action_form_not_instance(request, current_form, current_redirect, current_template):
    if request.method == 'POST':
        form = current_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(current_redirect)
    form = current_form()
    context = {
        'form': form,
        'not_profile': True,
    }
    return render(request, current_template, context)


def action_form_and_instance(request, current_form, current_redirect, current_template, instance):
    if request.method == 'POST':
        form = current_form(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(current_redirect)
    form = current_form(instance=instance)
    context = {
        'profile': get_profile(),
        'form': form,
        'pk': instance,
               }
    return render(request, current_template, context)


def home(request):
    if not get_profile():
        return redirect('create profile')
    context = {
        'expenses': Expense.objects.all(),
    }
    return render(request, 'home-with-profile.html', context)


def create_expense(request):
    return action_form_not_instance(request, CreateExpenseForm, 'home', 'expense-create.html')


def edit_expense(request, pk):
    return action_form_and_instance(request, CreateExpenseForm, 'home', 'expense-edit.html', Expense.objects.get(pk=pk))


def delete_expense(request, pk):
    return action_form_and_instance(request, DeleteExpense, 'home', 'expense-delete.html', Expense.objects.get(pk=pk))


def profile(request):
    current_profile = get_profile()
    budget_left = current_profile.budget - sum([p.price for p in Expense.objects.all()])
    expenses = len(Expense.objects.all())
    context = {
        'profile': get_profile(),
        'budget_left': budget_left,
        'expenses': expenses,
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    return action_form_not_instance(request, CreateProfileForm, 'profile', 'home-no-profile.html')


def profile_edit(request):
    return action_form_and_instance(request, CreateProfileForm, 'profile', 'profile-edit.html', get_profile())


def delete_profile(request):
    Expense.objects.all().delete()
    return action_form_and_instance(request, DeleteProfile, 'home', 'profile-delete.html', get_profile())


class ExpenseViews(views.View):
    def post(self, request):
        pass

    def get(self, request):
        expensive = Expense.objects.all()
        context = {
            'expensive': expensive
        }
        return render(request, 'views_expensive.html', context)
