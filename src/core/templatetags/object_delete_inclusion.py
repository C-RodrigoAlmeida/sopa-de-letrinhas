from django import template

register = template.Library()

@register.inclusion_tag('components/base_object_delete.html')
def object_delete_inclusion(form_title, object_type, object):
    return {
        'form_title': form_title,
        'object_type': object_type,
        'object': object
    }