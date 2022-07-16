from django import template

from Employees.application.models import Department

register = template.Library()


@register.inclusion_tag('tags/departments_list.html')
def departments_list_funk():
    departments = Department.objects \
        .prefetch_related('employee_set') \
        .all()
    # sokrashenie koda i uluchaet skorost

    return {
        'departments': departments,
    }
