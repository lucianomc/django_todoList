from django.urls import path

from . import views

app_name = 'todo_list'

urlpatterns = [
    path('cadastro/', views.create_user, name='cadastro'),
]
