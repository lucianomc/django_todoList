from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Tasks
from .models import TasksUsers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'creator', 'name', 'description',
                  'created_on', 'finish_in', 'priority', 'assigned_to')


class TaskUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TasksUsers
        fields = ('users', 'task', 'status')
