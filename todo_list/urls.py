from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (TaskCreateView, TaskDeleteView, TaskDetailView,
                    TaskListView, TaskUpdateView)

app_name = 'todo_list'

urlpatterns = [
    path('',
         login_required(TaskListView.as_view()), name='list_task'),

    path('tasks/create/',
         login_required(TaskCreateView.as_view()), name='create_task'),

    path('tasks/<int:pk>',
         login_required(TaskDetailView.as_view()), name='detail'),

    path('tasks/<int:pk>/update',
         login_required(TaskUpdateView.as_view()), name='update_task'),

    path('tasks/<int:pk>/delete',
         login_required(TaskDeleteView.as_view()), name='delete_task'),

]
