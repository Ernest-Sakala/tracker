from .views import AddHabitView, DeleteHabitView, HabitsView, UpdateHabitView, DailyHabitsView, WeeklyHabitsView, \
    MonthlyHabitsView
from django.urls import path


urlpatterns = [
    path('', AddHabitView.as_view(), name='add-habit'),
    path('habits', HabitsView.as_view(), name='habits'),
    path('delete/<pk>', DeleteHabitView.as_view()),
    path('update/<pk>', UpdateHabitView.as_view(), name='update'),
    path('daily', DailyHabitsView.as_view(), name='daily'),
    path('weekly', WeeklyHabitsView.as_view(), name='weekly'),
    path('monthly', MonthlyHabitsView.as_view(), name='monthly')
]
