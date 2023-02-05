from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User

class AccountCreationForm(UserCreationForm):
  
  class Meta:
    model = User
    fields = ('email',)


class AccountChangeForm(UserChangeForm):


	class Meta:
		model = User
		fields = ('rating', 'newsletter_subscription',)

		widgets = {
			'rating':forms.TextInput(attrs={'class':'form-control','style':'display:inherit; width:4rem;','type':'tel'}),
			'newsletter_subscription':forms.CheckboxInput(attrs={'class':'checkbox-control'}),
		}



