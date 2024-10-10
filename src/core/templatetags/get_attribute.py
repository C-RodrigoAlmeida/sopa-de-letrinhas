import types
from django import template

register = template.Library()

@register.filter(name="get_attribute")
def get_attribute(value, arg):
    
    attrs = arg.split('.')
    
    try:
        for attr in attrs:
            if isinstance(value, dict):
                value = value.get(attr, '')

            elif isinstance(value, list) and attr.isdigit():
                index = int(attr)
                value = value[index] if 0 <= index < len(value) else ''
                
            else:
                attribute = getattr(value, attr, None)
                
                if isinstance(attribute, types.MethodType):
                    value = attribute()
                else:
                    value = attribute

            if value == '':
                return ''
        
        return value
    except (AttributeError, IndexError):
        return ''
