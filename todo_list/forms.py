from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Tasks


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['name', 'description', 'finish_in', 'priority']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'maxlength': 128}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'maxlength': 128}),
            'finish_in': forms.DateInput(
                attrs={'class': 'form-control', 'maxlength': 128}),
            'priority': forms.Select(
                attrs={'class': 'form-control', 'maxlength': 128}),
        }
