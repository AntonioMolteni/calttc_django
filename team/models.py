from django.db import models
import os
from accounts.models import User
from PIL import Image

def user_filename(user):
	return user.display_name().replace(' ', '_')

def upload_location(instance, filename):
	"""
	Takes input instance to obtain a valid filename from user data 
	and appends it to the extension of FILENAME
	"""
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (user_filename(instance.user), ext)
	return os.path.join('profile_pictures', filename)


def content_file_name(name, filename):
	"""
	Returns a path constructed from name and the extension of FILENAME
	"""
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (name, ext)
	return os.path.join('profile_pictures', filename)

class Profile(models.Model):
	profile_picture = models.ImageField(upload_to=upload_location, blank=True)
	# related name is for use with the user model under accounts
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='team_profile', default=None, null=True, blank=True)
	position = models.CharField(max_length=75, blank=True)
	about = models.CharField(max_length=200, blank=True)
	show_rating = models.BooleanField(default=False) 
	executive = models.BooleanField(default=False)
	officer = models.BooleanField(default=False)
	competitive_team = models.BooleanField(default=False)


	# Code to Keep File Names Matching the Name Under Profile
	__original_profile_picture = None
	__original_user = None

	def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.__original_profile_picture = self.profile_picture
			self.__original_user = self.user

	def save(self, *args, **kwargs):
		if self.__original_user and self.__original_profile_picture:
			# "BASE_DIRECTORY/media/profile_pictures/input_file_name.jpeg"
			original_location = self.__original_profile_picture.path
			
			# "BASE_DIRECTORY/media/"
			new_location_prefix = original_location.split('/profile_pictures')[0]

			# "profile_pictures/user_display_name.input_file_ext
			new_name = content_file_name(user_filename(self.user), self.profile_picture.name)
			
			# "BASE_DIRECTORY/media/profile_pictures/user_display_name.input_file_ext"
			new_location = os.path.join(new_location_prefix, new_name)
			
			if self.profile_picture != self.__original_profile_picture:
				try:	
					os.remove(original_location)
				except:
					pass
			if self.user != self.__original_user:
				try:
					os.rename(original_location, new_location)
				except:
					pass
				self.profile_picture = new_name

		# call original save function
		super(Profile, self).save(*args, **kwargs)

		if self.profile_picture:
			image = Image.open(self.profile_picture)
			# convert to a square

			width, height = image.size
			new_width = min(width, height)
			new_height = new_width

			left = (width - new_width)/2
			top = (height - new_height)/2
			right = (width + new_width)/2
			bottom = (height + new_height)/2

			# Crop just the center of the image
			image = image.crop((left, top, right, bottom))

			# resize image to 500 by 500
			# https://stackoverflow.com/questions/7970637/how-to-resize-the-new-uploaded-images-using-pil-before-saving
			
			size = (500, 500)
			image = image.resize(size, Image.ANTIALIAS)
			image = image.save(self.profile_picture.path)
			
			# convert to .jpg
			# https://www.tutorialspoint.com/How-to-change-file-extension-in-Python
			jpg_path = content_file_name(os.path.splitext(self.profile_picture.path)[0], ".jpg")

			relative_jpg_path = jpg_path.split('media/')[-1]
			if str(self.profile_picture.path) !=  str(jpg_path):
				try:
					# conversion for images with transparency channel rgba
					image = image.convert('RGB')
					image.save(jpg_path)
					os.remove(self.profile_picture.path)
				except:
					pass
			self.profile_picture = relative_jpg_path
			super(Profile, self).save(*args, **kwargs)

		
	def get_id(self):
		return "profile_" + str(self.id)
