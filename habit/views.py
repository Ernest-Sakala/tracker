from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from habit.forms import HabitForm
# Create your views here.


class HabitView(View):

    greeting = "Good Day"

    def get(self, request):
        return render(request, 'habit/habits.html', {"greeting" : self.greeting})

    def post(self, request):

        habitModel = HabitForm(request.POST)

        if(habitModel.is_valid()):
            habitModel.save()


        return render(request, 'habits.html', {"message" : "Habit added successfully"})    