from django import template

register = template.Library()

@register.inclusion_tag('components/base_form.html')
def form_inclusion(form, form_title, submit_button_text):
    return {
        'form': form,
        'form_title': form_title,
        'submit_button_text': submit_button_text
    }
