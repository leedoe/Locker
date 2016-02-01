import datetime

from django import template

from LockerCustom.models import LockerDetail

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)