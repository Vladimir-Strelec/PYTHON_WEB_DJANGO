from django import template

register = template.Library()


@register.filter(name='even')
def even_numbers(value):
    """
    Return even number
    :param value: [3, 4, 5]
    :return: 4
    """
    return [n for n in value if n % 2 == 0]