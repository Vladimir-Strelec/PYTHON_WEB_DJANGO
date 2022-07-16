from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Django101.tasks.models import Task
#
#
# def home(request):
#     items = Task.objects.all()
#     items_strings = (f'<li>{t.title}</li>' for t in items)
#     items_string = ''.join(items_strings)
#     html = f"""
#         <H1>It works!</H1>
#         <ul>
#         {items_string}
#         </ul>
#     """
#     return HttpResponse(html)


def home(request):
    context = {
        'title': 'It works views!',
        'tasks': Task.objects.all()
    }
    return render(request, 'Home.html', context)