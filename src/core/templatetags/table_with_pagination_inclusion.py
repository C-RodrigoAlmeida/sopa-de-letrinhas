from django import template

register = template.Library()

@register.inclusion_tag('components/table_with_pagination.html')
def table_with_pagination_inclusion(title, headers, accessors, actions, object_list, model_name, pagination_controls, search, request):
    return {
        'title': title,
        'headers': headers,
        'accessors': accessors,
        'object_list': object_list,
        'table_url': f'{model_name}:list',
        'actions': actions,
        'pagination_controls': pagination_controls,
        'search': search,
        'request': request
    }