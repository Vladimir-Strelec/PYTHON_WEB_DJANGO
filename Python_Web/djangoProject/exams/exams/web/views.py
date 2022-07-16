from django.shortcuts import render, redirect

from exams.web.forms import CreateProfileForm, ProfileEditForm, ProfileDeleteForm, CreateExpenseForm, ExpenseEditForm, \
    ExpenseDeleteForm
from exams.web.models import Profile, Expense


def get_profile():
    profile = [p for p in Profile.objects.all()]
    if profile:
        return profile[0]
    return None


def action_forms(request, current_form, current_redirect, current_templates):
    if request.method == 'POST':
        form = current_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(current_redirect)
    form = current_form
    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, current_templates, context)


def action_forms_edit(request, current_form, current_redirect, current_templates, expense):
    if request.method == 'POST':
        form = current_form(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            return redirect(current_redirect)
    form = current_form(instance=expense)
    context = {
        'form': form,
        'expense': expense,

    }
    return render(request, current_templates, context)


def home_page(request):
    profile = get_profile()

    if not profile:
        return redirect('create profile')
    expense = Expense.objects.all()
    budget = profile.budget
    budget_left = profile.budget - sum(e.price for e in expense)
    context = {
        'expenses': expense,
        'budget': budget,
        'budget_left': budget_left,
    }

    return render(request, 'home-with-profile.html', context)


def create_expense_page(request):
    return action_forms(request, CreateExpenseForm, 'home_index', 'expense-create.html')


def edit_expense_page(request, pk):
    expense = Expense.objects.get(pk=pk)
    return action_forms_edit(request, ExpenseEditForm, 'home_index', 'expense-edit.html', expense)


def delete_expense_page(request, pk):
    expense = Expense.objects.get(pk=pk)
    return action_forms_edit(request, ExpenseDeleteForm, 'home_index', 'expense-delete.html', expense)


def profile_page(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(e.price for e in expenses)
    context = {
        'profile': profile,
        'budget_left': budget_left,
        'expenses': len(expenses),
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    return action_forms(request, CreateProfileForm, 'home_index', 'home-no-profile.html')


def profile_edit_page(request):
    return action_forms_edit(request, ProfileEditForm, 'profile page', 'profile-edit.html', get_profile())


def delete_profile_page(request):
    return action_forms_edit(request, ProfileDeleteForm, 'home_index', 'profile-delete.html', get_profile())


