from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from datetime import datetime, date

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
            'finish_in': forms.SelectDateWidget,
            'priority': forms.Select(
                attrs={'class': 'form-control'}),
        }

    def clean_finish_in(self):
        finish_in = self.cleaned_data['finish_in']
        if finish_in < date.today():
            raise forms.ValidationError("Data inválida")
        return finish_in
