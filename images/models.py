from django.db import models
import os

def carousel_upload_location(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (instance.name, ext)
	return os.path.join('carousel_images', filename)

def carousel_content_file_name(name, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (name, ext)
    return os.path.join('carousel_images', filename)

class CarouselImage(models.Model):
	image = models.ImageField(upload_to=carousel_upload_location)
	name = models.CharField(max_length=30, unique=True)

	__original_image = None
	__original_name = None

	def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.__original_image = self.image
			self.__original_name = self.name

	def save(self, *args, **kwargs):
		if self.__original_name and self.__original_image:
			new_name = carousel_content_file_name(self.name, self.image.name)
			new_name = new_name.replace(' ', '_')
			original_location = self.__original_image.path
			new_location_prefix = original_location.split('/carousel_images')[0]
			new_location = os.path.join(new_location_prefix, new_name)
			3
			if self.image != self.__original_image:
				os.remove(original_location)
				
			elif self.name != self.__original_name:
				os.rename(original_location, new_location)
				self.image = new_name

		super(CarouselImage, self).save(*args, **kwargs)

	def get_id(self):
		return "carousel_image_" + str(self.id)



def footer_upload_location(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (instance.name, ext)
	return os.path.join('footer_images', filename)

def footer_content_file_name(name, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (name, ext)
    return os.path.join('footer_images', filename)

class FooterImage(models.Model):
	image = models.ImageField(upload_to=footer_upload_location)
	name = models.CharField(max_length=30, unique=True)

	__original_image = None
	__original_name = None

	def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.__original_image = self.image
			self.__original_name = self.name

	def save(self, *args, **kwargs):
		if self.__original_name and self.__original_image:
			new_name = footer_content_file_name(self.name, self.image.name)
			new_name = new_name.replace(' ', '_')
			original_location = self.__original_image.path
			new_location_prefix = original_location.split('/footer_images')[0]
			new_location = os.path.join(new_location_prefix, new_name)
			3
			if self.image != self.__original_image:
				os.remove(original_location)
				
			elif self.name != self.__original_name:
				os.rename(original_location, new_location)
				self.image = new_name

		super(FooterImage, self).save(*args, **kwargs)

	def get_id(self):
		return "footer_image_" + str(self.id)