import re
from django import template

numeric_test = re.compile("^\d+$")
register = template.Library()

@register.filter(name='get_attribute')
def get_attribute(value: object | dict, arg: str):
    if isinstance(value, dict):
        return value[arg]
    elif isinstance(value, list):
        return value[int(arg)]
    return getattr(value, arg)
    