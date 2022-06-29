from .views import AddHabitView, DeleteHabitView, HabitsView, UpdateHabitView, DailyHabitsView, WeeklyHabitsView, \
    MonthlyHabitsView, TasksView, UpdateTaskView, StreakView
from django.urls import path


urlpatterns = [
    path('', AddHabitView.as_view(), name='add-habit'),
    path('habits', HabitsView.as_view(), name='habits'),
    path('delete/<pk>', DeleteHabitView.as_view()),
    path('update/<pk>', UpdateHabitView.as_view(), name='update'),
    path('daily', DailyHabitsView.as_view(), name='daily'),
    path('weekly', WeeklyHabitsView.as_view(), name='weekly'),
    path('monthly', MonthlyHabitsView.as_view(), name='monthly'),
    path('tasks/<pk>', TasksView.as_view(), name='tasks'),
    path('update_task/<pk>', UpdateTaskView.as_view(), name='update_task'),
    path('streak/<pk>', StreakView.as_view(), name='streak')
]
