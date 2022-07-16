from django.contrib import admin

from Employees.application.models import Employee, Department


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'egn', 'job_title', 'companies')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass