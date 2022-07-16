from django.http import HttpResponse
from django.shortcuts import render, redirect
import random


from Employees.application.models import Department, Employee


def home(request):
    context = {
        'numbers': [random.randint(1, 1023) for _ in range(16)]
    }
    return render(request, 'index.html', context)


def marketing_department(request, id):
    department = Department(
        name= f"Department {random.randint(1, 1024)}",)
    #  Department.objects.create(name=f"Create_department {random.randint(1, 1023)}",)
    #department.save()

    context = {
        'departments': Department.objects
            .prefetch_related('employee_set')
            .all(),
        'employees': Employee.objects.all(),
    }
    return render(request, 'marketing_department.html', context)


def go_to_marketing(request):
    return redirect(to='marketing department', id=1)