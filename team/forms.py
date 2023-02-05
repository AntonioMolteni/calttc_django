from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		
		widgets = {
			'profile_picture': forms.ClearableFileInput(),
			'position':forms.TextInput(attrs={'class':'form-control'}),
			'about':forms.Textarea(attrs={'class':'form-control', 'style':'height: 4rem;'}),
			'show_rating':forms.CheckboxInput(attrs={'class':'checkbox-control'}),
			'executive':forms.CheckboxInput(attrs={'class':'checkbox-control'}),
			'officer':forms.CheckboxInput(attrs={'class':'checkbox-control'}),
			'competitive_team':forms.CheckboxInput(attrs={'class':'checkbox-control'}),
		}
