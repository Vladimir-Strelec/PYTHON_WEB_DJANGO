from django.urls import path

from online_library.web.views import home, add_book, edit_book, book_details, profile, edit_profile, delete_profile, \
    create_profile, book_delete

urlpatterns = (
    path('', home, name='home'),

    path('add/', add_book, name='add book'),
    path('edit/<int:pk>', edit_book, name='edit book'),
    path('details/<int:pk>', book_details, name='book details'),
    path('book/delete/<int:pk>', book_delete, name='book delete'),

    path('profile/', profile, name='profile'),
    path('create/profile/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

)
