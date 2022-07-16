from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.core import validators
from django.shortcuts import render, redirect
from django import forms

from Employees.application.models import Employee, Department


def validate_positive(value):
    if value <= 0:
        raise ValidationError('Value most be positive')


# class EmployeeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=20,
#         widget=forms.TextInput(
#             attrs={'class': 'form-control'}
#         )
#     )
#
#     last_name = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={'class': 'form-control'}
#         )
#     )
#
#     age = forms.IntegerField(
#         required=False,
#         # widget=forms.NumberInput(
#         #     attrs={'type': 'range'}
#         # ),
#         validators=(
#             validate_positive,
#         )
#     )
#
#     egn = forms.IntegerField(
#         required=True,
#         validators=(
#             validate_positive, validators.MinValueValidator(10)
#         )
#     )
#
#     job_title = forms.ChoiceField(
#         choices=(
#             (1, 'Software Developer'),
#             (2, 'Qa Engineer'),
#             (3, 'Devops Specialist'),
#         )
#     )
#
#     companies = forms.ChoiceField(
#         choices=([(c, c) for c in Employee.COMPANIS]),
#     )
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        # widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control'})}


# def view_form(request):
#     context = {
#         'employee_form': EmployeeForm,
#     }
#     return render(request, 'template_form/form_get.html', context)

class EmployeeFormOrder(forms.Form):
    order_by_1 = forms.ChoiceField(
        choices=(
            ('first_name', 'First Name'),
            ('last_name', 'Last Name'),
        )
    )


def create_employee_post(request):
    return render(request, 'template_form/form_post.html')


# @csrf_exempt
# def create_employee_get(request):
#     if request.method == 'GET':
#         context = {
#             'employee_form': EmployeeForm()
#         }
#         return render(request, 'template_form/form_get.html', context)
#     else:
#         employee_form = EmployeeForm(request.POST)
#         if employee_form.is_valid():
#             return redirect('create employee post')
#         context = {
#             'employee_form': employee_form
#         }
#         return render(request, 'template_form/form_get.html', context)
@csrf_exempt
def create_employee_get(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES)
        if employee_form.is_valid():
            # emp = Employee(
            #     first_name=employee_form.cleaned_data['first_name'],
            #     last_name=employee_form.cleaned_data['last_name'],
            #     age=employee_form.cleaned_data['age'],
            #     egn=employee_form.cleaned_data['egn'],
            #     job_title=employee_form.cleaned_data['job_title'],
            #     companies=employee_form.cleaned_data['companies'],
            #     department_id=1,
            # )
            # emp = Employee(**employee_form.cleaned_data,
            #                department_id=3,)
            employee_form.save()
            return redirect('create employee post')

    employee_form_order = EmployeeFormOrder(request.GET)
    employee_form_order.is_valid()
    by_order = employee_form_order.cleaned_data.get('order_by_1', 'first_name')

    context = {
        'employee_form': EmployeeForm(),
        'employees': Employee.objects.order_by(by_order).all(),
        'employee_form_order': employee_form_order,
    }
    return render(request, 'template_form/form_get.html', context)


# @csrf_exempt
def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('create employee post')

    employee_form = EmployeeForm(instance=employee)
    context = {
        'employee': employee,
        'employee_form': employee_form,
    }
    return render(request, 'template_form/view_edit_form.html', context)
