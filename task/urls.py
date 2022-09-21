from django.urls import path
from task import views


app_name = "tasks"
urlpatterns = [
    path('task/<int:pk>/detail/', views.TaskDetail.as_view(), name='task_detail'),
    # path('task/<int:pk>/detail/', views.task_detail, name='task_detail'),

    path('', views.TaskList.as_view(), name='task_list'),
    # path('task_list/', views.task_list, name='task_list'),

    path('add_task/', views.AddTask.as_view(), name='add_task'),
    # path('add_task/', views.add_task, name='add_task'),

    # path('task/<pk>/edit/', views.EditTask.as_view(), name='edit_task'),
    path('task/<pk>/edit/', views.edit_task, name='edit_task'),

    path('todolist_list/', views.TodoListList.as_view(), name='todolist_list'),
    path('todolist/<pk>/detail/', views.TodoListDetail.as_view(), name='todolist_detail'),

    path('task_search/', views.task_search, name='task_search'),

    path('ajax/validate_task_name/', views.validate_task_name, name='validate_task_name')
]
