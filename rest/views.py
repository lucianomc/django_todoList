from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response

from todo_list.models import Tasks, TasksUsers

from .serializers import TaskSerializer, TaskUserSerializer, UserSerializer

# Create your views here.


class UserAPIListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()


class UserRudSet(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class TaskRudSet(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = TaskSerializer
    # queryset = Tasks.objects.all()

    def get_queryset(self):
        # return Tasks.objects.all()
        return Tasks.objects.filter(creator=self.request.user.id).order_by('id')

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class TaskAPIView(generics.CreateAPIView):
    # lookup_field = 'pk'
    serializer_class = TaskSerializer

    def get_queryset(self):
        # return Tasks.objects.all()
        return Tasks.objects.filter(creator=self.request.user.id)

    def perform_create(self, serializer):
        """To insert the user id in task's edit"""
        serializer.save(creator=self.request.user)


class TaskAPIListView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        # return Tasks.objects.all()
        return Tasks.objects.filter(creator=self.request.user.id).order_by('id')


class TaskUserViewSet(viewsets.ModelViewSet):
    #queryset = TasksUsers.objects.all()
    serializer_class = TaskUserSerializer

    def get_queryset(self):
        return TasksUsers.objects.filter(users=self.request.user)
