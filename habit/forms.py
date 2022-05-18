from django import forms
from django.forms import ModelForm
from .models import HabitModel


class HabitForm(ModelForm):

    class Meta:
        model = HabitModel
        fields = ('name', 'repetition', 'duration')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
            'repetition': forms.NumberInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateField()
        }
