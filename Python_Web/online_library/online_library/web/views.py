from django.shortcuts import render, redirect

from online_library.web.forms import CreateProfileForm, CreateBookForm, DeleteProfileForm
from online_library.web.models import Profile, Book


def get_profile():
    profile_current = Profile.objects.all()
    if profile_current:
        return profile_current[0]
    return None


def get_current_pk_book(pk):
    return Book.objects.get(pk=pk)


def action_form_create(request, current_form, current_redirect, template):
    if request.method == 'POST':
        form = current_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(current_redirect)
    form = current_form()
    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, template, context)


def action_form_edit(request, current_form, current_redirect, template, instance):
    if request.method == 'POST':
        form = current_form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(current_redirect)
    form = current_form(instance=instance)
    context = {
        'form': form,
        'book': instance,
        'profile': instance,

    }
    return render(request, template, context)


def home(request):
    profile_current = get_profile()
    books = Book.objects.all()
    if not profile_current:
        return redirect('create profile')
    context = {
        'books': books,
        'profile': profile_current,
    }
    return render(request, 'home-with-profile.html', context)


def add_book(request):
    return action_form_create(request, CreateBookForm, 'home', 'add-book.html')


def edit_book(request, pk):
    return action_form_edit(request, CreateBookForm, 'home', 'edit-book.html', get_current_pk_book(pk))


def book_details(request, pk):
    book = get_current_pk_book(pk)
    context = {
        'book': book
    }
    return render(request, 'book-details.html', context)


def book_delete(request, pk):
    get_current_pk_book(pk).delete()
    return redirect('home')


def profile(request):
    context = {
        'profile': get_profile()
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    return action_form_create(request, CreateProfileForm, 'home', 'home-no-profile.html')


def edit_profile(request):
    return action_form_edit(request, CreateProfileForm, 'home', 'edit-profile.html', get_profile())


def delete_profile(request):
    Book.objects.all().delete()
    return action_form_edit(request, DeleteProfileForm, 'create profile', 'delete-profile.html', get_profile())


