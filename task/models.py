from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from task.validators import datetime_must_be_in_futur


class TodoList(models.Model):
    label = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='todo_lists')

    class Meta:
        verbose_name = _('Todo list')
        verbose_name_plural = _('Todo lists')
        ordering = ('label', )

    def __str__(self):
        return self.label


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(
        validators=[], blank=True, null=True
    )
    done = models.BooleanField(default=False)

    todo_list = models.ForeignKey(
        TodoList, related_name='tasks', on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.name
