from django.contrib import admin

from habit.models import HabitModel

# Register your models here.


class HabitAdminConfig(admin.ModelAdmin):

    model = HabitModel
    list_display = ('id','name', 'repetition','duration' , 'completed', 'start_date', 'finish_date', 'broken', 'streak')


admin.site.register(HabitModel, HabitAdminConfig)
