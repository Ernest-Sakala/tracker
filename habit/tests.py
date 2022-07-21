import datetime
from itertools import groupby

from django.test import TestCase

# Create your tests here.
from habit.models import HabitModel, TaskModel


class TestClass(TestCase):

    def test_habit_model(self):
        model = HabitModel.objects.create(name="Run", start_date=datetime.datetime.now(),
                                          finish_date=datetime.datetime.now())

        self.assertEquals("Run", str(model))

    def test_task_model(self):
        habit = HabitModel.objects.create(name="Run", start_date=datetime.datetime.now(),
                                          finish_date=datetime.datetime.now())

        model = TaskModel.objects.create(done=True, task_date=datetime.datetime.now(), habit=habit)

        self.assertEquals(True, model.done)

    def test_streak_number(self):

        habit = HabitModel.objects.create(name="Run Yeah", start_date=datetime.datetime.now(),
                                          finish_date=datetime.datetime.now())

        TaskModel.objects.create(done=True, task_date=datetime.datetime.now(), habit=habit)
        TaskModel.objects.create(done=True, task_date=datetime.datetime.now(), habit=habit)
        TaskModel.objects.create(done=True, task_date=datetime.datetime.now(), habit=habit)

        habit = HabitModel.objects.filter(id=habit.id)
        tasks = TaskModel.objects.filter(habit=habit[0])

        number_tasks = number_formatted(tasks)

        def consecutive_one(data) -> int:
            if number_tasks.__contains__(1):
                return max(len_iter(run) for val, run in groupby(data) if val)
            else:
                return 0

        longest_streak = consecutive_one(number_tasks)

        self.assertEquals(3, longest_streak)


def number_formatted(tasks):
    number_tasks = []

    for task in tasks:
        if task.done:
            number_tasks.append(1)
        else:
            number_tasks.append(0)
    return number_tasks


def len_iter(items):
    return sum(1 for _ in items)
