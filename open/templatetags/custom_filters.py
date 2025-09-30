from django import template

register = template.Library()

@register.filter(name='split')
def split(value, arg):
    """Divide una cadena por el separador dado"""
    if value:
        return value.split(arg)
    return []

@register.filter(name='trim')
def trim(value):
    """Elimina espacios en blanco al inicio y final"""
    if value:
        return value.strip()
    return value
