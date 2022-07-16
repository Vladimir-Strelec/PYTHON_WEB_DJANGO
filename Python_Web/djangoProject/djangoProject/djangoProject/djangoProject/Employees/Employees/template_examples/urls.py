from django.urls import path

from Employees.template_examples.views import index

urlpatterns = [
    path('', index, name='templates index'),
]