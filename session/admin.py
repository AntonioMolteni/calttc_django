from django.contrib import admin
from .models import Session

class SessionAdmin(admin.ModelAdmin):
	model = Session
	list_display = ('session_type','location','time','duration')
	list_filter = ('session_type',)
admin.site.register(Session, SessionAdmin)