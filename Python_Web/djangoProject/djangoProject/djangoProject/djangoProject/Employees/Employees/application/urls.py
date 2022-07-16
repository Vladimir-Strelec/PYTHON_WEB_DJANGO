
from django.urls import path
from Employees.application.views import home, marketing_department, go_to_marketing


urlpatterns = [
    path('', home, name='Go to home'),
    path('<int:id>', marketing_department, name='marketing department'),
    path('go_to_marketing/', go_to_marketing, name='to marketing')
]
