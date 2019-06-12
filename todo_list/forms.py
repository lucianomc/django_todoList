from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User


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
