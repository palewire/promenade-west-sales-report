import statistics
from django import template
from django.utils import timezone
register = template.Library()


@register.simple_tag
def now():
    return timezone.now()


@register.simple_tag
def percent_change(old, new):
    return ((new - old) / old)*100


@register.simple_tag
def average(object_list, attr="count"):
    values = [o[attr] for o in object_list]
    return statistics.mean(values)
