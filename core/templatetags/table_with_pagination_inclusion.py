from django import template

register = template.Library()

@register.inclusion_tag('components/table_with_pagination.html')
def table_with_pagination_inclusion(title, headers, acessors, object_list, model_name, pagination_controls, search):
    return {
        'title': title,
        'headers': headers,
        'acessors': acessors,
        'object_list': object_list,
        'table_url': f'{model_name}_list',
        'row_update': f'{model_name}_update',
        'row_delete': f'{model_name}_delete',
        'row_details': f'{model_name}_details',
        'controls': pagination_controls,
        'search': search,
    }