from django.urls import path

from Django101.tasks.views import home

urlpatterns = [
    path('', home),
]