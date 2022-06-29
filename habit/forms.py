from django import forms
from django.forms import ModelForm, DateInput
from django.utils import timezone

from .models import HabitModel


class HabitForm(ModelForm):

    class Meta:
        model = HabitModel
        fields = ('name', 'duration', 'start_date', 'finish_date')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format="%d/%m/%Y"),
            'finish_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
        }
