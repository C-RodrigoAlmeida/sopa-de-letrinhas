from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def sort_by(context, index):
    """
    Generates a URL for sorting by the given field.
    Toggling between ascending and descending order.
    """
    request = context['request']
    current_sort = request.GET.get('sort', '')
    accessors = context['accessors']
    
    if accessors[index] != 'action':
        if current_sort == accessors[index]:
            new_sort = f'-{accessors[index]}'  # Toggle to descending
        elif current_sort == f'-{accessors[index]}':
            new_sort = accessors[index]  # Toggle to ascending
        else:
            new_sort = accessors[index]  # Default ascending sort
    else:
        new_sort = None
    
    # Ensure we handle `action` or other cases
    query_params = request.GET.copy()
    query_params['sort'] = new_sort if new_sort else 'default'  # Fallback to default

    return f'?{query_params.urlencode()}'
