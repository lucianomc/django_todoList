
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from rest_framework import reverse as api_reverse


class Tasks(models.Model):
    """
        Model relationed to task, consist in a creator, a name for the task 
        (name), a description for the task (description), a date of creation 
        (created_at), a date of update (update_at), a limit date of task 
        (finish_in), a priority of task (priority) and a relacionship many to 
        many to assigned users to execute this task (assigned_to).
    """

    PRIORITY = (
        (3, 'Baixa'),
        (5, 'Normal'),
        (8, 'Alta'),
    )
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='admin')
    name = models.CharField(
        max_length=32,
        default='No name')
    description = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    finish_in = models.DateField()
    priority = models.PositiveIntegerField(choices=PRIORITY)
    assigned_to = models.ManyToManyField(
        User,
        blank=True,
        through='TasksUsers',
        related_name='associated')

    class Meta:
        verbose_name = "Task"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('todo_list:detail', kwargs={'pk': self.id})
        # return "/todolist/tasks/%i" % (self.id)

    # def get_api_url(self, request=None):
    #     return api_reverse('todo_list:detail', kwargs={'pk': self.id}, request=request)


class TasksUsers(models.Model):
    """
        This model relates, users and tasks. After create task, the creator 
        has to associate the others users to doing this task.
    """
    STATUS = (
        (0, 'Pendente'),
        (1, 'Concluído')
    )
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey('Tasks', on_delete=models.CASCADE)
    status = models.BooleanField(choices=STATUS, default=False)

    def __str__(self):
        return f"{self.users}, {self.task}"
