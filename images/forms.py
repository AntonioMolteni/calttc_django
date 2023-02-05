from .models import CarouselImage
from .models import FooterImage
from django import forms

class CarouselImageForm(forms.ModelForm):
	class Meta:
		model = CarouselImage
		fields = '__all__'
		
	def clean_image(self):
		image = self.cleaned_data.get("image")
		if image:
			ext = image.name.split('.')[-1]
			if not ext in ["webp", "png", "jpg"]:
				raise forms.ValidationError("This image has the '{e}' extension. Use 'webp', 'png' or 'jpg'.  Use 'webp' for optimal performance".format(e=ext))
		return image

class FooterImageForm(forms.ModelForm):
	class Meta:
		model = FooterImage
		fields = '__all__'
		
	def clean_image(self):
		image = self.cleaned_data.get("image")
		if image:
			ext = image.name.split('.')[-1]
			if not ext in ["webp", "png", "jpg"]:
				raise forms.ValidationError("This image has the '{e}' extension. Use 'webp', 'png' or 'jpg'.  Use 'webp' for optimal performance".format(e=ext))
		return image
