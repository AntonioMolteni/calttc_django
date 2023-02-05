from django.db import models

DayChoices = (
	('U','Sunday'),
  ('M','Monday'),
	('T','Tuesday'),
  ('W','Wednesday'),
	('R','Thursday'),
  ('F','Friday'),
	('S','Saturday'),
)

LocationChoices = (
	('RSFField','RSF Field House'),
  ('RSFCombat','RSF Combatives Room'),
)

AvailabilityChoices = (
	('A', 'Anyone (No Drop-In Fee Required)'),
	('MD','Members or Drop-In Fee'),
	('M', 'Members Only'),
)

class TimeSlot(models.Model):
	time_slot = models.CharField(max_length=100, blank=True)
	day = models.CharField(max_length=9, choices=DayChoices, blank=True)
	location = models.CharField(max_length=20, choices=LocationChoices, blank=True)
	availability = models.CharField(max_length=15, choices=AvailabilityChoices, blank=True)
	open_play = models.BooleanField(default=True)
	novice_training = models.BooleanField(default=False)
	intermediate_training = models.BooleanField(default=False)
	advanced_training = models.BooleanField(default=False)
	tournaments = models.BooleanField(default=False)