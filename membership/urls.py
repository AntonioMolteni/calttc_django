from django.urls import path
from . import views

urlpatterns = [
	path("", views.membership, name="membership"),
	path("edit_dues_link/<dues_link_id>", views.edit_dues_link, name="edit-dues-link"),

  path("register", views.register, name="register"),
  path("unregister", views.unregister, name="unregister"),
  path("approve_membership/<user_email>", views.approve_membership, name="approve-membership"),
  path("refuse_membership/<user_email>", views.refuse_membership, name="refuse-membership"),

  
] 