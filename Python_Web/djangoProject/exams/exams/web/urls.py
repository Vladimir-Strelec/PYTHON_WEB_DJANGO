from django.urls import path

from exams.web.views import create_expense_page, edit_expense_page, delete_expense_page, profile_page, \
    profile_edit_page, delete_profile_page, home_page, create_profile

urlpatterns = (
    path('', home_page, name='home_index'),

    path('create/', create_expense_page, name='create expense page'),
    path('edit/<int:pk>/', edit_expense_page, name='edit expense page'),
    path('delete/<int:pk>/', delete_expense_page, name='delete expense page'),

    path('profile/', profile_page, name='profile page'),
    path('no profile/', create_profile, name='create profile'),
    path('profile/edit/', profile_edit_page, name='profile edit page'),
    path('profile/delete/', delete_profile_page, name='delete profile page'),
)