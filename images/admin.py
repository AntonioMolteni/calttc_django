from django.contrib import admin

from .forms import CarouselImageForm
from .models import CarouselImage
from .forms import FooterImageForm
from .models import FooterImage

class ImagesAdmin(admin.ModelAdmin):
	model = CarouselImage
	form = CarouselImageForm
	list_display = ('name','image')
	def has_add_permission(self, request, obj=None):
		return False
	def has_delete_permission(self, request, obj=None):
		return False
admin.site.register(CarouselImage, ImagesAdmin)

class ImagesAdmin(admin.ModelAdmin):
	model = FooterImage
	form = FooterImageForm
	list_display = ('name','image')
	def has_delete_permission(self, request, obj=None):
		return False
admin.site.register(FooterImage, ImagesAdmin)