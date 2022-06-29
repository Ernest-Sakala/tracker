from django.db import models
from model_utils import Choices


# Create your models here.
class HabitModel(models.Model):
    class Meta:
        db_table = "habit"

    DURATION = Choices("DAILY", "WEEKLY", "MONTHLY")

    name = models.CharField(max_length=255)
    number_completed = models.IntegerField(default=0)
    duration = models.CharField(max_length=255, choices=DURATION, default=DURATION.DAILY)
    completed = models.BooleanField(default=False)
    start_date = models.DateField()
    finish_date = models.DateField()
    broken = models.BooleanField(default=False)
    streak = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class TaskModel(models.Model):
    class Meta:
        db_table = "task"

    completed = models.BooleanField(default=False)
    task_date = models.DateField()
    habit = models.ForeignKey(HabitModel, on_delete=models.CASCADE)

    def __str__(self):
        return "Task"
