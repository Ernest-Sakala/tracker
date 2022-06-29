from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.edit import DeleteView, UpdateView
from habit.forms import HabitForm
from habit.models import HabitModel, TaskModel
import datetime
from itertools import groupby


# Create your views here.


class AddHabitView(View):

    def get(self, request):
        form = HabitForm()

        return render(request, 'add_habit.html', {'form': form})

    def post(self, request):
        data = request.POST

        habit_exists = HabitModel.objects.filter(name=data.get('name')).exists()

        if habit_exists:
            return redirect('/')

        start_date = data.get('start_date')
        finish_date = data.get('finish_date')
        duration = data.get('duration')

        new_start_date = start_date.replace('-', '/')
        new_finish_date = finish_date.replace('-', '/')

        date_format = "%Y/%m/%d"

        d1 = datetime.datetime.strptime(new_start_date, date_format).date()
        d2 = datetime.datetime.strptime(new_finish_date, date_format).date()
        d = d1

        step = ""
        if duration.__eq__("DAILY"):
            step = datetime.timedelta(days=1)
        elif duration.__eq__("WEEKLY"):
            step = datetime.timedelta(days=7)
        elif duration.__eq__("MONTHLY"):
            step = datetime.timedelta(days=30)

        habit_model = HabitForm(data)

        if habit_model.is_valid():
            habit = habit_model.save()

            saved_habit = HabitModel.objects.filter(name=habit)

            while d <= d2:
                date = d.strftime(date_format)

                new_date = date.replace('/', '-')
                task = TaskModel(completed=False, task_date=new_date, habit=saved_habit[0])
                task.save()
                d += step

        return redirect('/habits')


class HabitsView(View):

    def get(self, request):
        habits = HabitModel.objects.all()

        print(habits)

        return render(request, 'habits.html', {'habits': habits})


class DailyHabitsView(View):

    def get(self, request):
        habits = HabitModel.objects.filter(duration="DAILY")
        return render(request, 'habits.html', {'habits': habits})


class WeeklyHabitsView(View):

    def get(self, request):
        habits = HabitModel.objects.filter(duration="WEEKLY")

        return render(request, 'habits.html', {'habits': habits})


class MonthlyHabitsView(View):

    def get(self, request):
        habits = HabitModel.objects.filter(duration="MONTHLY")

        return render(request, 'habits.html', {'habits': habits})


class DeleteHabitView(DeleteView):
    model = HabitModel
    success_url = "/habits"


class UpdateHabitView(UpdateView):
    model = HabitModel

    template_name = "HabitModel_form.html"

    fields = [
        "streak",
        "completed"
    ]

    success_url = "/habits"


class TasksView(View):
    model = TaskModel

    def get(self, request, pk):
        tasks = TaskModel.objects.filter(habit=pk)

        return render(request, 'tasks.html', {'tasks': tasks})


class UpdateTaskView(UpdateView):
    model = TaskModel

    template_name = "TaskModel_form.html"

    fields = [
        "completed"
    ]

    success_url = "/habits"


class StreakView(View):

    def get(self, request, pk):
        habit = HabitModel.objects.filter(id=pk)
        tasks = TaskModel.objects.filter(habit=habit[0])

        number_tasks = []

        for task in tasks:
            if task.completed:
                number_tasks.append(1)
            else:
                number_tasks.append(0)

        def len_iter(items):
            return sum(1 for _ in items)

        def consecutive_one(data) -> int:
            if number_tasks.__contains__(1):
                return max(len_iter(run) for val, run in groupby(data) if val)
            else:
                return 0;

        longest_streak = consecutive_one(number_tasks)

        return render(request, 'streak.html', {'streak': longest_streak})
