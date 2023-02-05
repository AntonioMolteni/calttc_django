from django.urls import path
from . import views

urlpatterns = [
	path("", views.schedule, name="schedule"),
	path("edit_schedule", views.edit_schedule, name="edit-schedule"),
]