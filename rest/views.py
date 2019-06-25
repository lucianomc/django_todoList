from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from todo_list.models import Tasks, TasksUsers

from .serializers import TaskSerializer, TaskUserSerializer, UserSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer


class TaskUserViewSet(viewsets.ModelViewSet):
    queryset = TasksUsers.objects.all()
    serializer_class = TaskUserSerializer
