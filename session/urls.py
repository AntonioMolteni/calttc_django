
from django.urls import path
from . import views

urlpatterns = [
  path("", views.sessions, name="sessions"),
  path("add_sessions", views.add_sessions, name="add-sessions"),
  path("edit_session/<session_id>", views.edit_session, name="edit-session"),
  path("delete_session/<session_id>", views.delete_session, name="delete-session"),
  path("roster_by_rating/<session_id>", views.roster_by_rating, name="roster-by-rating"),

  path("drop/<session_id>", views.drop, name="drop"),
  path("sign_up/<session_id>", views.sign_up, name="sign-up"),

  
]