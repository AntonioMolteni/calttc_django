
from django.urls import path
from . import views

urlpatterns = [
  path("compose_newsletter", views.compose_newsletter, name="compose-newsletter"),
  path("subscribe", views.subscribe, name="subscribe"),
  path("unsubscribe", views.unsubscribe, name="unsubscribe"),
  path("unsubscribe_external", views.unsubscribe_external, name="unsubscribe-external"),
  path("subscribe_external", views.subscribe_external, name="subscribe-external"),
  path("export_newsletter_csv", views.export_newsletter_csv, name="export-newsletter-csv"),
]