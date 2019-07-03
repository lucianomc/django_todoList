from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from todo_list.models import Tasks, TasksUsers

from .serializers import TaskSerializer, TasksUserSerializer, UserSerializer

# Create your views here.


class UserAPIListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class UserRudView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
        # return User.objects.filter(id=self.request.user.id)


class TaskRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = TaskSerializer
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated,)
    # queryset = Tasks.objects.all()

    def get_queryset(self):
        # return Tasks.objects.all()
        return Tasks.objects.filter(creator=self.request.user.id).order_by('id')

#     # def get_serializer_context(self, *args, **kwargs):
#     #     return {"request": self.request}


class TaskAPICreateView(generics.CreateAPIView):
    # lookup_field = 'pk'
    serializer_class = TaskSerializer

    # def get_queryset(self):
    #     return Tasks.objects.all()
#         return Tasks.objects.filter(creator=self.request.user.id)

    def perform_create(self, serializer):
        """To insert the user id in task's edit"""
        serializer.save(creator=self.request.user)


class TaskAPIListView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        # return Tasks.objects.all()
        return Tasks.objects.filter(creator=self.request.user.id).order_by('id')


class TasksUserAPIListView(generics.ListAPIView):
    # queryset = TasksUsers.objects.all()
    serializer_class = TasksUserSerializer

    def get_queryset(self):
        # return TasksUsers.objects.all()
        return TasksUsers.objects.filter(users=self.request.user)


class TasksUserRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = TasksUserSerializer

    def get_queryset(self):
        return User.objects.all()
        # return User.objects.filter(id=self.request.user.id)


class TaskUserAPICreateView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = TasksUserSerializer

    def perform_create(self, serializer):
        """To insert the user id in task's edit"""
        serializer.save(creator=self.request.user)
