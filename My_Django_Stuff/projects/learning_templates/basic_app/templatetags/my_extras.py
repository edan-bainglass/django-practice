from django import template

register = template.Library()


@register.filter
def cut(value: str, arg: str) -> str:
    """Cut out all values of 'arg' from the string."""
    return value.replace(arg, '')
