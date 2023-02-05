
from django.urls import path
from . import views

urlpatterns = [
  path("add_announcement", views.add_announcement, name="add-announcement"),
  path("edit_announcement/<announcement_id>", views.edit_announcement, name="edit-announcement"),
  path("delete_announcement/<announcement_id>", views.delete_announcement, name="delete-announcement"),
  path("discord_announcement", views.discord_announcement, name="discord-announcement"),
]