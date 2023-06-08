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
		fields = ('rating',)

		widgets = {
			'rating':forms.TextInput(attrs={'class':'form-control rating','style':'display:inherit; width:4rem;','type':'tel'}),
		}


ExportChoices = (
  ('U','Users'),
  ('M','Members'),
)
		
class ExportEmailCSVForm(forms.Form):
	recipients = forms.ChoiceField(label='Recipients', choices=ExportChoices, widget=forms.Select(attrs={'class':'form-control'}))
 


