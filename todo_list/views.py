from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from todo_list.forms import UserModelForm


# Create your views here.


def index(request):
    users = User.objects.all().order_by('first_name')
    context = {'users': users}
    return render(request, 'todo_list/index.html', context)


def create_user(request):
    form = UserModelForm(request.POST or None)
    context = {'form': form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo_list:index'))
    return render(request, 'todo_list/cadastro.html', context)
