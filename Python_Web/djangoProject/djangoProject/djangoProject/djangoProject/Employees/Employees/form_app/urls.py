from django.urls import path

from Employees.form_app.views import create_employee_get, create_employee_post, edit_employee

urlpatterns = (
    # path('', view_form, name='form'),
    path('get/', create_employee_get, name='create employee get'),
    path('post/', create_employee_post, name='create employee post'),
    path('edit/<int:pk>/', edit_employee, name='edit employee'),
)