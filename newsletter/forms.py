from django import forms
from .models import Newsletter

ExportChoices = (
  ('OU','Opted-In Users'),
	('OM','Opted-In Members'),
  ('AM','All Members'),
)

class NewsletterForm(forms.ModelForm):
	class Meta:
		model = Newsletter
		fields = '__all__'
		
		widgets = {
			'subject':forms.TextInput(attrs={'class':'form-control'}),
			'image':forms.ClearableFileInput(),
			'content':forms.Textarea(attrs={'class':'form-control'}),
			'test_user_email':forms.TextInput(attrs={'class':'form-control'}),
			'recipients':forms.Select(attrs={'class':'form-control'}),
			'gmail_csv':forms.ClearableFileInput(),
			'unsubscribe_link':forms.CheckboxInput(attrs={'class':'checkbox-control'}),
		}
		

class ExportNewsletterCSVForm(forms.Form):
	recipients = forms.ChoiceField(label='Recipients', choices=ExportChoices, widget=forms.Select(attrs={'class':'form-control'}))
 