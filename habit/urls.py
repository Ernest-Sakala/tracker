from .views import HabitView
from django.urls import path


urlpatterns = [
    path('', HabitView.as_view()),
  
]