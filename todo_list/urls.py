from django.urls import path

from . import views

app_name = 'todo_list'

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit_login),
    path('users/', views.UserListView.as_view()),
    path('cadastro/', views.UserCreateView.as_view(), name='cadastro'),
    path('tasks/', views.TaskListView.as_view()),
    path('tasks/create/', views.TaskCreateView.as_view()),
    path('tasks/<int:pk>', views.TaskDetailView.as_view(), name='detail'),
]
