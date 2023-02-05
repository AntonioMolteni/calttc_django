from django.urls import path
from . import views

urlpatterns = [
	path("", views.membership, name="membership"),
  path("approve_drop_in/<user_email>", views.approve_drop_in, name="approve-drop-in"),
  path("refuse_drop_in/<user_email>", views.refuse_drop_in, name="refuse-drop-in"),

  path("register", views.register, name="register"),
  path("unregister", views.unregister, name="unregister"),
  path("approve_membership/<user_email>", views.approve_membership, name="approve-membership"),
  path("refuse_membership/<user_email>", views.refuse_membership, name="refuse-membership"),

  
] 