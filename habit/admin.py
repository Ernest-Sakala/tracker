from django.contrib import admin

from habit.models import HabitModel

# Register your models here.


class HabitAdminConfig(admin.ModelAdmin):

    model = HabitModel
    list_display = ('id','name', 'repeatition','duration' , 'duration_type', 'completed', 'start_date', 'finnish_date', 'broken', 'streak')


admin.site.register(HabitModel, HabitAdminConfig)
