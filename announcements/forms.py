from django import forms
from django.forms import ModelForm
from . models import Announcement


class AnnouncementAdminForm(ModelForm):
  class Meta:
    model = Announcement
    fields = '__all__'
    
class AddAnnouncementForm(ModelForm):
  class Meta:
    model = Announcement
    fields = '__all__'
    
    widgets = {
      'title':forms.TextInput(attrs={'class':'form-control'}),
      'content':forms.Textarea(attrs={'class':'form-control'}),
      'link_text':forms.TextInput(attrs={'class':'form-control'}),
      'link_url':forms.TextInput(attrs={'class':'form-control'}),
    }

class EditAnnouncementForm(ModelForm):
  class Meta:
    model = Announcement
    fields = '__all__'
    
    widgets = {
      'title':forms.TextInput(attrs={'class':'form-control'}),
      'content':forms.Textarea(attrs={'class':'form-control'}),
      'link_text':forms.TextInput(attrs={'class':'form-control'}),
      'link_url':forms.TextInput(attrs={'class':'form-control'}),

    }