# custom_filters.py
from django import template

register = template.Library()

@register.filter
def replace(value, arg):
    return value.replace(arg, '<span class="highlight">{}</span>'.format(arg))
