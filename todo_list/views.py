from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView
from django.views.generic.list import ListView

from .forms import TaskModelForm, UserModelForm
from .models import Tasks, TasksUsers

# from rest_framework import viewsets

# from todo_list.serializers import (TaskSerializer, TaskUserSerializer,
#                                    UserSerializer)


# Create your views here.
# definifir as views dentro da pasta views e colocar o __init__.py.
# Dentro do init fazer o from views import a classe


def index(request):
    return render(request, 'todo_list/index.html')


def submit_login(request):
    if request.POST:
        usern = request.POST['username']
        passw = request.POST['password']
        print(usern)
        print(passw)
        # user = authenticate(username=usern, password=passw)
        # if user is not None:
        #     login(request, user)
        #     return redirect('login/')
        # else:
        #     messages.error(request, 'Usuário/Senha inválidos')
    return reverse_lazy('todo_list:index')

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


class TaskListView(ListView):
    model = Tasks
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Tasks
    context_object_name = 'task'


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('id')
#     serializer_class = UserSerializer


# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Tasks.objects.all().order_by('id')
#     serializer_class = TaskSerializer


# class TaskUserViewSet(viewsets.ModelViewSet):
#     queryset = TasksUsers.objects.all()
#     serializer_class = TaskUserSerializer
