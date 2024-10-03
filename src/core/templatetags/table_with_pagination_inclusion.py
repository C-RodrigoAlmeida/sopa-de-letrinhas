from django import template

register = template.Library()

@register.inclusion_tag('components/table_with_pagination.html')
def table_with_pagination_inclusion(title, headers, acessors, actions, object_list, model_name, pagination_controls, search):
    return {
        'title': title,
        'headers': headers,
        'acessors': acessors,
        'object_list': object_list,
        'table_url': f'{model_name}:list',
        'actions': actions,
        'controls': pagination_controls,
        'search': search,
    }