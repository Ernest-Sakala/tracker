from .views import AddHabitView, DeleteHabitView, HabitsView, UpdateHabitView
from django.urls import path


urlpatterns = [
    path('', AddHabitView.as_view()),
    path('habits', HabitsView.as_view()),
    path('delete/<pk>', DeleteHabitView.as_view()),
    path('update/<pk>', UpdateHabitView.as_view(), name='update')
]
