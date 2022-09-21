import datetime

from django import forms
from django.utils import timezone

from task.models import Task


class AddTaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        initial=timezone.now(),
        widget=forms.SelectDateWidget,
    )

    class Meta:
        model = Task
        exclude = ('done',)


class EditTaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.SelectDateWidget)

    class Meta:
        model = Task
        exclude = ()


CHOICES = (
    (None, "In progress or done"),
    (True, "Done"),
    (False, "In progress"),
)


class TaskSearchForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, empty_value=None)
    deadline_start = forms.DateField(required=False, widget=forms.SelectDateWidget)
    deadline_end = forms.DateField(required=False, widget=forms.SelectDateWidget)
    done = forms.NullBooleanField(
        required=False,
        widget=forms.RadioSelect(choices=CHOICES),
    )
