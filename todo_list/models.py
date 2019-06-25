
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Tasks(models.Model):

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


class TasksUsers(models.Model):
    STATUS = (
        (0, 'Pendente'),
        (1, 'Concluído')
    )
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey('Tasks', on_delete=models.CASCADE)
    status = models.BooleanField(choices=STATUS, default=False)

    def __str__(self):
        return f"{self.users}, {self.task}"
