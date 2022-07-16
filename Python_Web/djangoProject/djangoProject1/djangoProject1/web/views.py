from django.shortcuts import render


def home_index(request):
    x = request
    return render(request, 'home-with-profile.html')


def creat_not(request):
    return render(request, 'note-create.html')


def edit_note(request):
    return render(request, 'note-edit.html')


def delete_note(request):
    return render(request, 'note-delete.html')


def note_details(request):
    return render(request, 'note-details.html')


def profile(request):
    return render(request, 'profile.html')


