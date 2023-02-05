from django.urls import path
from . import views

urlpatterns = [
	path("", views.team, name="team"),
	path("edit_profiles", views.edit_profiles, name="edit-profiles"),
]