from django.urls import path
from . import views

urlpatterns = [
	path("edit_carousel_images", views.edit_carousel_images, name="edit-carousel-images"),
	path("edit_footer_images", views.edit_footer_images, name="edit-footer-images"),
] 