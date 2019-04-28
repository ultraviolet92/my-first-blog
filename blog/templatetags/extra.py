from django import template

register = template.Library()

@register.filter
def related_deltas(obj, lesson):
    return obj.is_active(obj, lesson)