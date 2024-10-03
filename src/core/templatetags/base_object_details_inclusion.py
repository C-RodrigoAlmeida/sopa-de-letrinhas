from django import template

register = template.Library()

@register.inclusion_tag('components/base_object_details.html')
def base_object_details_inclusion(object: object, model_description: str, field_names: dict, control_buttons: dict) -> dict:
    return {
        'object': object,
        'model_description': model_description,
        'field_names': field_names,
        'control_buttons': control_buttons
        
    }