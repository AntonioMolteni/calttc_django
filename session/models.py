from datetime import timedelta, datetime
from django.db import models
from django.utils import timezone
from accounts.models import User

SessionTypeChoices = (
  ('NT','Novice Training'),
  ('IT','Intermediate Training'),
  ('AT','Advanced Training'),
  ('RR','Round-Robin Tournament'),
  ('TO','Tournament'),
  ('CT','Competitive Team Tryouts'),
)

LocationChoices = (
	('RSFField','RSF Field House'),
  ('RSFCombat','RSF Combatives Room'),
)

# cutoff for session sign_ups in minutes
cutoff = 5

today = timezone.now().date()
eight_months_ago = today - timedelta(days=8*30)  # Assuming 30 days per month

# Filter the members queryset based on the last login date range
users = User.objects.filter(last_login__range=[eight_months_ago, today])
    

class Session(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  session_type = models.CharField(max_length=30, choices=SessionTypeChoices, default='')
  location = models.CharField(max_length=30, choices=LocationChoices, default='RSF Field House')
  time = models.DateTimeField()
  duration = models.PositiveIntegerField()
  capacity = models.IntegerField()
  note = models.CharField(max_length=300, default=None, blank=True, null=True)
  is_closed = models.BooleanField(default = False)
  is_cancelled = models.BooleanField(default=False)
  coaches = models.ManyToManyField(User, related_name='coaching', limit_choices_to= {'is_staff': True})
  players = models.ManyToManyField(User, related_name='playing', blank=True)
  queue = models.ManyToManyField(User, related_name='queuing', blank=True)

  def __str__(self):
    end_time = self.time + timedelta(minutes=int(self.duration))
    return self.time.strftime("%-I:%M") + "-" + end_time.strftime("%-I:%M %p") + self.time.strftime(" %a %b %-d")
  
  def get_players(self):
    return self.players.filter(is_active=True).order_by('-is_member', '-has_berkeley_email', 'sign_up_date',)[:self.capacity] 
  
  def get_wait_list(self):
    return self.players.filter(is_active=True).order_by('-is_member', '-has_berkeley_email', 'sign_up_date')[self.capacity:]
  
  def get_queue(self):
    return self.queue.filter(is_active=True).order_by('-is_member', '-has_berkeley_email', 'date_joined')[:self.capacity]
  
  def get_session_type(self):
    return "Session Type: " + self.get_session_type_display()
    
  def get_coaches(self):
    if self.coaches.count() > 1:
      output_string = "Coaches: "
    else:
      output_string = "Coach: "
    comma_string = ", ".join([coach.display_name() for coach in self.coaches.all()])
    return output_string + comma_string
  
  def get_location(self):
    return "Location: " + self.get_location_display()
  
  def get_capacity(self):
    return "Capacity: " + str(self.capacity)
  
  def get_remaining_slots(self):
    return "Remaining Slots: " + str(max(self.capacity-self.players.count(), 0))
  
  def get_id(self):
    return "session_" + str(self.id)
  
  def is_full(self):
    return self.capacity-self.players.count() <= 0
  
  def is_available(self):
    return datetime.now() <= self.time - timedelta(minutes=cutoff) and not self.is_closed and not self.is_cancelled

  def is_training(self):
    return self.session_type == "NT" or self.session_type == "IT" or self.session_type == "AT"
  
  def is_competitive_team_tryouts(self):
    return self.session_type == "CT"
    
  def is_tournament(self):
    return self.session_type == "RR" or self.session_type == "TO"
  

  