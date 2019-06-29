from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .forms import TaskModelForm
from .models import Tasks, TasksUsers


class TaskCreateView(CreateView):
    model = Tasks
    form_class = TaskModelForm
    success_url = reverse_lazy('todo_list:list_task')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(UpdateView):
    model = Tasks
    fields = ['name', 'description', 'finish_in', 'priority']
    success_url = reverse_lazy('todo_list:list_task')


class TaskListView(ListView):
    model = Tasks

    def get_context_data(self):
        context = {
            'creator': Tasks.objects.filter(
                creator=self.request.user),
            'assigned': Tasks.objects.filter(
                assigned_to=self.request.user)
        }
        return context


class TaskDetailView(DetailView):
    model = Tasks
    context_object_name = 'task'


class TaskDeleteView(DeleteView):
    model = Tasks
    success_url = reverse_lazy('todo_list:list_task')


class TaskUserCreateView(CreateView):
    model = TasksUsers
    fields = ['users', 'status']
    #fields = '__all__'
    success_url = reverse_lazy('todo_list:list_task')

    def form_valid(self, form):
        form.instance.task_id = self.kwargs['pk']
        # print(self.kwargs['pk'])
        return super(TaskUserCreateView, self).form_valid(form)


class TaskUserUpdateView(UpdateView):
    model = TasksUsers
    fields = ['status']
    success_url = reverse_lazy('todo_list:list_task')
