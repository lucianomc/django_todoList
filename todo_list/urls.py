from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView

app_name = 'todo_list'

urlpatterns = [
    path('',
         login_required(TaskListView.as_view()), name='list_task'),
    path('tasks/create/',
         login_required(TaskCreateView.as_view()), name='create_task'),
    path('tasks/<int:pk>',
         login_required(TaskDetailView.as_view()), name='detail'),
    path('tasks/<int:pk>/update',
         login_required(TaskUpdateView.as_view()), name='update_task')
]
