from django.db import models
from django.utils import timezone


# Create your models here.
class HabitModel(models.Model):
    class Meta:
        db_table = "habit"

    name = models.CharField(max_length=255)
    repetition = models.IntegerField()
    number_completed = models.IntegerField(default=0)
    duration = models.CharField(max_length=255)
    # frequency = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()
    broken = models.BooleanField(default=False)
    streak = models.IntegerField(default=0)

    def __str__(self):
        return self.name
