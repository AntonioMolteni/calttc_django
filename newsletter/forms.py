from django import forms

RecipientChoices = (
	('TU','Test User'),
  ('OU','Opted-In Users'),
	('OM','Opted-In Members'),
  ('AM','All Members'),
)

class NewsletterForm(forms.Form):
	subject = forms.CharField(label='Subject', max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
	content = forms.CharField(label='Content', max_length=1500, widget=forms.Textarea(attrs={'class':'form-control'}))
	test_user_email = forms.CharField(label='Test User Email',max_length=100, required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
	recipients = forms.ChoiceField(label='Recipients', choices=RecipientChoices, widget=forms.Select(attrs={'class':'form-control'}))
 