from django import template

register = template.Library()


@register.filter
def lower(value):
    return value.lower()

@register.filter
def upper(value):
    return value.upper()

@register.filter()
def capitalize(value):
    return value.capitalize()