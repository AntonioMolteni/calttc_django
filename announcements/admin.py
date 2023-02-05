from django.contrib import admin
from .models import Announcement

class AnnouncementAdmin(admin.ModelAdmin):
	model = Announcement
	list_display = ('title','content',)
	ordering = ('title',)
admin.site.register(Announcement,AnnouncementAdmin)