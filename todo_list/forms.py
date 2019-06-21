from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Tasks


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username', 'first_name', 'last_name', 'password']
        # exclude =
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'maxlength': 128}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'maxlength': 128}),
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'maxlength': 128}),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control', 'maxlength': 128}),
        }
        # error_messages = {}


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['creator', 'name', 'description', 'finish_in', 'priority']
        widgets = {
            'creator': forms.Select(
                attrs={'class': 'form-control', 'maxlength': 128}),
            'name': forms.TextInput(
                attrs={'class': 'form-control', 'maxlength': 128}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'maxlength': 128}),
            'finish_in': forms.DateInput(
                attrs={'class': 'form-control', 'maxlength': 128}),
            'priority': forms.Select(
                attrs={'class': 'form-control', 'maxlength': 128}),
        }
