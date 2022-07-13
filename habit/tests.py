import datetime

from django.test import TestCase

# Create your tests here.
from habit.models import HabitModel, TaskModel


def add(num, num2):
    return num + num2


class TestClass(TestCase):

    def test_AddNumbers(self):
        self.assertEquals(add(2, 2), 4)

    def test_habit_model(self):
        model = HabitModel.objects.create(name="Run", start_date=datetime.datetime.now(),
                                          finish_date=datetime.datetime.now())

        self.assertEquals("Run", str(model))

    def test_task_model(self):
        habit = HabitModel.objects.create(name="Run", start_date=datetime.datetime.now(),
                                          finish_date=datetime.datetime.now())

        model = TaskModel.objects.create(completed=True, task_date=datetime.datetime.now(), habit=habit)

        self.assertEquals(True, model.completed)