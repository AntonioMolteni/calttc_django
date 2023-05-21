from django.db import models
class DuesLink(models.Model):
	link_text = models.CharField(max_length=80, default=None, blank=True, null=True)
	link_url = models.URLField(max_length=300, default=None, blank=True, null=True)
	link_opens_in_new_tab = models.BooleanField(default=True)