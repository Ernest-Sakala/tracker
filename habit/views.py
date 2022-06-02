from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
from habit.forms import HabitForm
from habit.models import HabitModel
from django.views.generic.edit import DeleteView, UpdateView


# Create your views here.


class AddHabitView(View):

    def get(self, request):
        form = HabitForm()

        return render(request, 'add_habit.html', {'form': form})

    def post(self, request):
        habitModel = HabitForm(request.POST)

        if (habitModel.is_valid()):
            habitModel.save()

        return redirect('/habits')


class HabitsView(View):

    def get(self, request):
        habits = HabitModel.objects.all()

        return render(request, 'habits.html', {'habits': habits})


class DailyHabitsView(View):

    def get(self, request):
        habits = HabitModel.objects.filter(duration="Daily")

        print(habits)

        return render(request, 'habits.html', {'habits': habits})


class WeeklyHabitsView(View):

    def get(self, request):
        habits = HabitModel.objects.filter(duration="Weekly")

        print(habits)

        return render(request, 'habits.html', {'habits': habits})


class MonthlyHabitsView(View):

    def get(self, request):
        habits = HabitModel.objects.filter(duration="Monthly")

        print(habits)

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
