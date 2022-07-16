from django.urls import path

from test_exam.web.views import home, add_note, edit_note, delete_note, note_details, profile, create_profile, \
    delete_profile

urlpatterns = (
    path('', home, name='home'),

    path('add/', add_note, name='add note'),
    path('edit/<int:pk>/', edit_note, name='edit_note'),
    path('delete/<int:pk>/', delete_note, name='delete note'),
    path('details/<int:pk>/', note_details, name='note details'),

    path('profile', profile, name='profile'),
    path('create profile/', create_profile, name='create profile'),
    path('delete profile/', delete_profile, name='delete profile'),

)