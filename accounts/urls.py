from django.urls import include, path
from accounts import views

urlpatterns = [
	path('login/', views.login, name="login"),
	path('logout/', views.logout, name = 'logout'),
	path('settings/', views.settings, name = 'account-settings'),
	path("manage_users",views.manage_users, name="manage-users"),
	path("privacy_policy",views.privacy_policy, name="privacy-policy"),
  path("export_email_csv", views.export_email_csv, name="export-email-csv"),

]