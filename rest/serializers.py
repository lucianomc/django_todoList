from django.contrib.auth.models import User
from rest_framework import serializers

from todo_list.models import Tasks
from todo_list.models import TasksUsers

# from todo_list.views import TaskListView, TaskDetailView


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'first_name',
            'last_name'
        ]
        read_only_fields = ['id', 'username']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = [
            'id',
            'creator',
            'name',
            'description',
            'created_on',
            'finish_in',
            'priority',
            'assigned_to'
        ]
        read_only_fields = ['id', 'creator']


class TaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TasksUsers
        fields = [
            'users',
            'task',
            'status'
        ]
