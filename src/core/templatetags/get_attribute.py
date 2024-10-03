import re
import types
from django import template
numeric_test = re.compile("^\d+$")
register = template.Library()

@register.filter(name='get_attribute')
def get_attribute(value: object | dict, arg: str | types.MethodType) -> str:
    if isinstance(value, dict):
        return value[arg]
    
    elif isinstance(value, list):
        return value[int(arg)]
    
    elif isinstance(getattr(value, arg), types.MethodType):
        return getattr(value, arg)()
    
    return getattr(value, arg)
