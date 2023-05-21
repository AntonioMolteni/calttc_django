from django.contrib import admin

from .forms import NewsletterForm
from .models import Newsletter

class NewsletterAdmin(admin.ModelAdmin):
	model = Newsletter
	form = NewsletterForm
	list_display = ('subject',)
	readonly_fields=('subject', 'content', 'image','recipients', 'test_user_email', 'gmail_csv')
	def has_add_permission(self, request, obj=None):
		return False
	def has_delete_permission(self, request, obj=None):
		return False
admin.site.register(Newsletter, NewsletterAdmin)