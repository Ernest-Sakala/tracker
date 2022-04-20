from django.forms import ModelForm
from .models import HabitModel

class  HabitForm(ModelForm):

    class Meta:
        model = HabitModel
        fields = '__all__'
