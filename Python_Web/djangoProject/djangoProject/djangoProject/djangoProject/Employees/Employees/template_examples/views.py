from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from Employees.application.models import Employee, Department


def index(request):
    context = {
        'numbers': [123, 200, 300],
        'status': 'iT woR k',
        'employees': Employee.objects.order_by('-first_name', 'last_name').all(),
        'lorem': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium iure qui reiciendis totam? Accusamus blanditiis consequatur debitis delectus facere facilis\
         fuga incidunt laborum nihil, nostrum, omnis sapiente tempora tenetur, voluptate!',
        'departments_all': [d.name for d in Department.objects.all()]
    }
    return render(request, 'template_example/index.html', context)
