from django.db import models

# Create your models here.
class HabitModel(models.Model):

    class Meta:
        db_table = "habit"

    name = models.CharField(max_length=255)
    repeatition = models.IntegerField()
    duration = models.IntegerField()
    duration_type = models.CharField(max_length=255)
    completed = models.BooleanField()
    start_date = models.DateField()
    finnish_date = models.DateField()
    broken = models.BooleanField()
    streak = models.IntegerField()