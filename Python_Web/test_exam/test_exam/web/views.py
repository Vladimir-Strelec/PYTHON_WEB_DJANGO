from django.shortcuts import render, redirect

from test_exam.web.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from test_exam.web.models import Profile, Note


def get_profile():
    current_profile = Profile.objects.all()
    if current_profile:
        return current_profile[0]
    return None


def action_create_form(request, current_form, current_redirect, template):
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


def action_edit_form(request, current_form, current_redirect, template, instance):
    if request.method == 'POST':
        form = current_form(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(current_redirect)
    form = current_form(instance=instance)
    context = {
        'form': form,
        'not_pk': instance,
    }
    return render(request, template, context)


def home(request):
    all_notes = Note.objects.all()
    if not get_profile():
        return redirect('create profile')
    context = {
        'all_notes': all_notes,
    }
    return render(request, 'home-with-profile.html', context)


def add_note(request):
    return action_create_form(request, CreateNoteForm, 'home', 'note-create.html')


def edit_note(request, pk):
    note_pk = Note.objects.get(pk=pk)
    return action_edit_form(request, EditNoteForm, 'home', 'note-edit.html', note_pk)


def delete_note(request, pk):
    note_pk = Note.objects.get(pk=pk)
    return action_edit_form(request, DeleteNoteForm, 'home', 'note-delete.html', note_pk)


def note_details(request, pk):
    current_not = Note.objects.get(pk=pk)

    context = {
        'curren_not': current_not,
        'not_pk': current_not,
    }
    return render(request, 'note-details.html', context)


def profile(request):
    profiles = Profile.objects.all()
    all_notes = Note.objects.all()
    context = {
        "profiles": profiles,
        "all_notes": len(all_notes),
    }
    return render(request, 'profile.html', context)


def create_profile(request):
    return action_create_form(request, CreateProfileForm, 'home', 'home-no-profile.html')


def delete_profile(request):
    instance_profile = get_profile()
    Profile.delete(instance_profile)
    Note.objects.all().delete()
    return redirect('create profile')
