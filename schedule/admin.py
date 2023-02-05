from django.contrib import admin
from .models import TimeSlot

class ScheduleAdmin(admin.ModelAdmin):
	model = TimeSlot
	list_display = ('day', 'time_slot', 'location', 'open_play', 'novice_training', 'intermediate_training', 'advanced_training', 'tournaments')
admin.site.register(TimeSlot, ScheduleAdmin)