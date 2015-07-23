import datetime
import re

from dateutil.parser import parse
from django import template;


register = template.Library()


@register.simple_tag
def short_name(name):
    match = re.search(r'[\w]+\s\w', name)
    return '%s.' % (match.group(0)) if match else name


@register.simple_tag
def decorate_name(name):
    return '*'.join(['%s' % char for char in name])


@register.simple_tag
def multiply_by_1000(arg):
    return '%d * 1000 = %d' % (arg, arg * 1000)


@register.simple_tag
def month_name(month_integer):
    return datetime.date(2015, month_integer, 1).strftime(
        '%B') if 0 < month_integer <= 12 else 'invalid integer'


@register.simple_tag
def full_month_name(month_name):
    return parse(month_name).strftime("%B")
