from django import template

register = template.Library()

@register.inclusion_tag('components/base_object_delete.html')
def object_delete_inclusion(title, object_type, object):
    return {
        'title': title,
        'object_type': object_type,
        'object': object
    }