from django.utils import timezone
from django import template
register = template.Library()


@register.simple_tag
def now():
    return timezone.now()


@register.simple_tag
def percent_change(old, new):
    return ((new - old) / old)*100
