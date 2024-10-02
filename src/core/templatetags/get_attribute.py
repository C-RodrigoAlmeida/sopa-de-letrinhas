import re
from django import template
numeric_test = re.compile("^\d+$")
register = template.Library()

@register.filter(name='get_attribute')
def get_attribute(value: object | dict, arg: str) -> str:
    if isinstance(value, dict):
        return value[arg]
    
    elif isinstance(value, list):
        return value[int(arg)]
    
    elif hasattr(getattr(value, arg), 'all'):
        related_items = getattr(value, arg).all()[:4]
        items = [str(v) for v in related_items[:3]]
        
        if len(related_items) > 3:
            items.append('...')
        
        return ', '.join(items)

    return getattr(value, arg)
