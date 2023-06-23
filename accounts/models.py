from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import Group

from django.utils import timezone
from datetime import timedelta



class UserManager(BaseUserManager):
	
	ordering = ('email',)
	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError('Users require an email field')
		email = self.normalize_email(email)
		user = self.model(
			email = email,
			is_active = True,
			**extra_fields
   		)
		if password:
			user.set_password(password)
		user.save(using = self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)
	
	# used in manage users
	def query_last_login_within_8_months(self):
		today = timezone.now().date()
		eight_months_ago = today - timedelta(days=8*30)
		return User.objects.filter(last_login__range=[eight_months_ago, today])
		

class User(AbstractBaseUser, PermissionsMixin):
	
	username = None
	email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
	has_berkeley_email = models.BooleanField(default=False)
	first_name = models.CharField(max_length=254, null=True, blank=True)
	last_name = models.CharField(max_length=254, null=True, blank=True)
	is_registered = models.BooleanField(default=False)
	is_member = models.BooleanField(default=False)
	rating = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(4000)], default=0)

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	date_joined = models.DateTimeField(auto_now_add=True)
	sign_up_date = models.DateTimeField(null=True, blank=True)
	

	class Meta:
		ordering = ['first_name']

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
 
#  check useradmin for code that updates the is_staff and is_admin when the form is submitted
	def save(self, *args, **kwargs):
		staff_group = Group.objects.get(name='Staff')
		admin_group = Group.objects.get(name='Admin')
		if self.is_staff:
			self.groups.add(staff_group)
		else:
			self.groups.remove(staff_group)
		if self.is_admin:
			self.groups.add(admin_group)
		else:
			self.groups.remove(admin_group)
		if self.is_superuser:
			self.is_admin = True
			self.is_staff = True
		self.has_berkeley_email = "@berkeley.edu" in self.email
		super(User, self).save(*args, **kwargs)

	# check if a user has a team profile associated with it in settings
	def get_profile(self):
		if(hasattr(self, 'team_profile')):
			return self.team_profile
		return None

	def display_name(self):
		if self.first_name and self.last_name:
			return self.first_name + " " + self.last_name
		elif self.first_name and not self.last_name:
			return self.first_name
		elif not self.first_name and self.last_name:
			return self.last_name
		else:
			return ""

	def __str__(self):
		return self.display_name() + " | " + self.email
