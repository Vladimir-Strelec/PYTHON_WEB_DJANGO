from django.urls import path

from djangoProject1.web.views import home_index, creat_not, edit_note, delete_note, note_details, profile

urlpatterns = (
    path('', home_index, name='home index'),
    path('add/', creat_not, name='create note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delete/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', note_details, name='note details'),
    path('profile', profile, name='profile'),

)
