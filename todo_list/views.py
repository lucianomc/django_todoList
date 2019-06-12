from django.shortcuts import render

from todo_list.forms import UserModelForm

# Create your views here.


def create_user(request):
    form = UserModelForm(request.POST or None)
    context = {'form': form}
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, 'todo_list/cadastro.html', context)
