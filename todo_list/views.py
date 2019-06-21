from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.list import ListView
from rest_framework import viewsets

from todo_list.forms import TaskModelForm, UserModelForm
from todo_list.serializers import (TaskSerializer, TaskUserSerializer,
                                   UserSerializer)

from .models import Tasks, TasksUsers

# Create your views here.


def index(request):
    return render(request, 'todo_list/index.html')


# def create_user(request):
#     form = UserModelForm(request.POST or None)
#     context = {'form': form}
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('todo_list:index'))
#     return render(request, 'todo_list/cadastro.html', context)


class UserCreateView(CreateView):
    template_name = 'todo_list/user_form.html'
    form_class = UserModelForm
    success_url = reverse_lazy('todo_list:index')


class UserListView(ListView):
    template_name = 'todo_list/user_list.html'
    model = User
    context_object_name = 'users'


class TaskCreateView(CreateView):
    model = Tasks
    form_class = TaskModelForm
    success_url = reverse_lazy('todo_list:index')


class TaksListView(ListView):
    model = Tasks
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Tasks
    context_object_name = 'task'


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Tasks.objects.all().order_by('id')
    serializer_class = TaskSerializer


class TaskUserViewSet(viewsets.ModelViewSet):
    queryset = TasksUsers.objects.all()
    serializer_class = TaskUserSerializer
