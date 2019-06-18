from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView

from todo_list.forms import UserModelForm

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
    template_name = 'todo_list/cadastro.html'
    form_class = UserModelForm
    success_url = reverse_lazy('todo_list:index')


class UserListView(ListView):
    template_name = 'todo_list/users.html'
    model = User
    context_object_name = 'users'
