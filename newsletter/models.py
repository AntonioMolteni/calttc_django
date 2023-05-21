from django.db import models
import os

def upload_location(instance,filename):
	return os.path.join('newsletter', filename)

RecipientChoices = (
	('TU','Test User'),
  ('OU','Opted-In Users'),
	('OM','Opted-In Members'),
  ('AM','All Members'),
	('LI','Gmail CSV List')
)

class Newsletter(models.Model):
	subject = models.CharField(max_length=100)
	content = models.CharField(max_length=2000, blank=True)
	image = models.ImageField(upload_to=upload_location, blank=True)
	test_user_email = models.CharField(max_length=100, blank = True)
	recipients = models.CharField(max_length=20, choices=RecipientChoices, )
	gmail_csv = models.FileField(upload_to=upload_location, blank=True,)
	unsubscribe_link = models.BooleanField(default=True)


