from datetime import date

from django import template

register = template.Library()


@register.filter
def time_left(task_datetime):
    if not task_datetime:
        return 'Not given'

    today = date.today()
    delta = task_datetime.date() - today

    if delta.days > 1:
        out = f"In {delta.days} days"
    elif delta.days == 1:
        out = "Tomorrow"
    elif delta.days == 0:
        out = "Today"
    else:
        out = "You're late !"

    return out
