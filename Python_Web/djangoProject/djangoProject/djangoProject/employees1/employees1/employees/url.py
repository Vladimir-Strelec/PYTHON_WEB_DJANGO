from django.urls import path

from employees1.employees.views import home, marketing_department_1, hr_department_2, production_department_3, \
    go_to_home

urlpatterns = (path('<int:id>/', marketing_department_1, name='marketing department'),
               path('lol/', hr_department_2, name='hr department 2'),
               path('go/', go_to_home, name='go to home'),
               path('', home, name='index'),

)