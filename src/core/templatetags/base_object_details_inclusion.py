from django import template

register = template.Library()

@register.inclusion_tag('components/base_object_details.html')
def base_object_details_inclusion(object: object, model_description: str, model_name: str, field_names: dict) -> dict:
    return {
        'object': object,
        'model_description': model_description,
        'field_names': field_names,
        'object_delete': f'{model_name}_delete',
        'object_update': f'{model_name}_update',
        'object_list': f'{model_name}_list',
    }