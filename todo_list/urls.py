from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import TaskListView, TaskDetailView, TaskCreateView

app_name = 'todo_list'

urlpatterns = [
    path('', login_required(TaskListView.as_view()), name='list_task'),
    # path('submit/', views.submit_login),
    # path('users/', views.UserListView.as_view()),
    # path('cadastro/', views.UserCreateView.as_view(), name='cadastro'),
    #path('tasks/', TaskListView.as_view()),
    path('tasks/create/', login_required(TaskCreateView.as_view()), name='create_task'),
    path('tasks/<int:pk>', login_required(TaskDetailView.as_view()), name='detail'),
]
