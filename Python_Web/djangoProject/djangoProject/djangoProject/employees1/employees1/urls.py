from django.contrib import admin
from django.urls import path, include

from employees.views import home, go_to_home
from employees1.employees import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(url)),
]
