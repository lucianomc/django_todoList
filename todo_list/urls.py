from django.urls import path

from . import views

app_name = 'todo_list'

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.UserListView.as_view()),
    path('cadastro/', views.UserCreateView.as_view(), name='cadastro'),
]
