from django.contrib import admin


from .models import Tasks
from .models import TasksUsers

# Register your models here.
admin.site.register(Tasks)
admin.site.register(TasksUsers)
