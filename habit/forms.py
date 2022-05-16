from django import forms
from django.forms import ModelForm
from .models import HabitModel


class HabitForm(ModelForm):

    class Meta:
        model = HabitModel
        fields = ('name','repeatition', 'duration', 'duration_type')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'repeatition': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration_type': forms.TextInput(attrs={'class': 'form-control'}),
        }
