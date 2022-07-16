from django.urls import path

from Exam_preparation.web.views import home, create_expense, edit_expense, delete_expense, profile, profile_edit, \
    delete_profile, create_profile, ExpenseViews

urlpatterns = (
    path('', home, name='home'),

    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>', edit_expense, name='edit expense'),
    path('delete/<int:pk>', delete_expense, name='delete expense'),

    path('profile/', profile, name='profile'),
    path('create/profile/', create_profile, name='create profile'),
    path('profile/edit', profile_edit, name='profile edit'),
    path('profile/delete', delete_profile, name='delete profile'),
    path('Expense/Views', ExpenseViews.as_view(), name='ExpenseViews'),
)
