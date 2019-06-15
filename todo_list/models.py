from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tasks(models.Model):
    admin = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    finish_in = models.DateField()
    priority = models.DecimalField(decimal_places=0, max_digits=1)
