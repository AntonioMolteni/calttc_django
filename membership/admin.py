from django.contrib import admin
from .models import DuesLink

class DuesLinkAdmin(admin.ModelAdmin):
	model = DuesLink
	list_display = ('link_text','link_url',)
	ordering = ('link_text',)
	def has_add_permission(self, request, obj=None):
		return False
	def has_delete_permission(self, request, obj=None):
		return False
admin.site.register(DuesLink,DuesLinkAdmin)