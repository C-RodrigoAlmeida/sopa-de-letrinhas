from django import template

register = template.Library()

@register.inclusion_tag('components/base_object_details.html')
def base_object_details_inclusion(object, object_type, fields, object_name):
    return {
        'object': object,
        'object_type': object_type,
        'fields': fields,
        'object_delete': f'{object_name}_delete',
        'object_update': f'{object_name}_update',
        'object_list': f'{object_name}_list',
    }