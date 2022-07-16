from django import template

register = template.Library()


@register.filter(name='capitalize')
def capitalize(value):
    """
        first character do it big
    """
    value = str(value)
    return value[0].upper() + value[1:].lower()
