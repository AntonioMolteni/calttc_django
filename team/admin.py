from django.contrib import admin

from .forms import ProfileForm
from .models import Profile

class TeamAdmin(admin.ModelAdmin):
	model = Profile
	form = ProfileForm
	list_display = ('user','position', 'profile_picture', 'executive', 'officer', 'competitive_team',)
	
admin.site.register(Profile, TeamAdmin)