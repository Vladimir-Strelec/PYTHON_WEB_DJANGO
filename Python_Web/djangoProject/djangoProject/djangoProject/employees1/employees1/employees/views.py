import random
import textwrap

from django.http import HttpResponse
from django.shortcuts import render, redirect


#
# def home(request):
#     html = f"<h1>{request.method} This is home!</h1>"
#     return HttpResponse(
#         html,
#     )
from django.urls import reverse_lazy


def home(request):
    number = random.randint(1, 1024)
    # context = {
    #     'number_range': number,
    # }

    context = {
        'numbers': [random.randint(1, 100) for _ in range(16)]
    }
    return render(request, 'index.html', context)


def go_to_home(request):
   return redirect(to='marketing department', id=1)


def marketing_department_1(request, id):
    return render(request, 'second.html')


def hr_department_2(request):
    return HttpResponse(f'This is hr_department')


def production_department_3(request):
    return HttpResponse(f'This is production_department {id}')

