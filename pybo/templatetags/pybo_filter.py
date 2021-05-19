from django import template

register = template.Library()

@register.filter
def sub(value, org):
  return value - org
