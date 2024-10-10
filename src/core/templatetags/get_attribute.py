import re
import types
from django import template

register = template.Library()

@register.filter(name='get_attribute')
def get_attribute(value, arg):
    print(f"Accessing: {arg} in {value}")

    if isinstance(value, dict):
        return value.get(arg, '')

    if isinstance(value, list) and arg.isdigit():
        index = int(arg)
        return value[index] if 0 <= index < len(value) else ''

    try:
        attribute = getattr(value, arg)
        
        if isinstance(attribute, types.MethodType):
            return attribute()
        return attribute
    
    except AttributeError:
        return ''

