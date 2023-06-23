from django.db import models

class Announcement(models.Model):
	title = models.CharField(max_length=80, default=None, blank=True, null=True)
	content = models.CharField(max_length=500, default=None, blank=True, null=True)
	link_text = models.CharField(max_length=80, default=None, blank=True, null=True)
	link_url = models.URLField(max_length=300, default=None, blank=True, null=True)
	link_opens_in_new_tab = models.BooleanField(default=True)
	on_home_page = models.BooleanField(default=False)
	on_schedule_page = models.BooleanField(default=False)
	on_sessions_page = models.BooleanField(default=False)
	on_membership_page = models.BooleanField(default=False)
	on_team_page = models.BooleanField(default=False)
