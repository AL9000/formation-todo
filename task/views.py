from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from task.forms import AddTaskForm, EditTaskForm, TaskSearchForm
from task.models import Task, TodoList


def task_list(request):
    tasks = Task.objects.all()
    context = {
        'object_list': tasks,
    }
    return render(request, 'task/task_list.html', context)


class TaskList(ListView):
    model = Task


# Solution 1 : function based view
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    context = {
        'task': task,
    }
    return render(request, 'task/task_detail.html', context)


class TaskDetail(DetailView):
    model = Task


def add_task(request):
    form = AddTaskForm(request.POST or None)
    if form.is_valid():
        task = form.save()
        return redirect(reverse('tasks:task_detail', args=(task.pk,)))
    context = {
        'form': form,
    }
    return render(request, 'task/add_task.html', context)


class AddTask(CreateView):
    model = Task
    form_class = AddTaskForm
    template_name = 'task/add_task.html'

    def get_success_url(self):
        return reverse('tasks:task_detail', args=(self.object.pk,))


def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    form = EditTaskForm(request.POST or None, instance=task)
    if form.is_valid():
        task = form.save()
        return redirect(reverse('tasks:task_detail', args=(task.pk,)))
    context = {
        'task': task,
        'form': form,
    }
    return render(request, 'task/edit_task.html', context)


class EditTask(UpdateView):
    model = Task
    form_class = EditTaskForm
    template_name = 'task/edit_task.html'

    def get_success_url(self):
        return reverse('tasks:task_detail', args=(self.object.pk,))


class TodoListList(ListView):
    model = TodoList


class TodoListDetail(DetailView):
    model = TodoList


def task_search(request):
    form = TaskSearchForm(request.GET or None)

    tasks = Task.objects.all()
    if form.is_valid():

        name = form.cleaned_data.get('name')
        if name:
            tasks = tasks.filter(name__icontains=name)

        deadline_start = form.cleaned_data.get('deadline_start')
        if deadline_start:
            tasks = tasks.filter(deadline__gte=deadline_start)

        deadline_end = form.cleaned_data.get('deadline_end')
        if deadline_end:
            tasks = tasks.filter(deadline__lte=deadline_end)

        done = form.cleaned_data.get('done')
        if done is not None:
            tasks = tasks.filter(done=done)

    return render(
        request,
        'task/task_search.html',
        {
            'tasks': tasks,
            'form': form,
        }
    )


def validate_task_name(request):
    task_name = request.GET.get('task_name')
    data = {
        'is_taken': Task.objects.filter(name__iexact=task_name).exists()
    }
    return JsonResponse(data)
