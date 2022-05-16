
from django.db import models
from django.utils import timezone

# Create your models here.
class HabitModel(models.Model):

    class Meta:
        db_table = "habit"

    name = models.CharField(max_length=255)
    repeatition = models.IntegerField()
    duration = models.IntegerField()
    duration_type = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    start_date = models.DateField(default=timezone.now())
    finnish_date = models.DateField(default=timezone.now())
    broken = models.BooleanField(default=False)
    streak = models.IntegerField(default=0)