from django.contrib import admin

from task.models import Task, TodoList

admin.site.register(Task)
admin.site.register(TodoList)
