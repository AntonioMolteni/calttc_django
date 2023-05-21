from django import forms
from django.forms import ModelForm
from . models import DuesLink

class EditDuesLinkForm(ModelForm):
  class Meta:
    model = DuesLink
    fields = '__all__'
    
    widgets = {
      'link_text':forms.TextInput(attrs={'class':'form-control'}),
      'link_url':forms.TextInput(attrs={'class':'form-control'}),
    }