from django import forms
from django.forms import ModelForm
from .models import Session
from datetime import timedelta, datetime


class SessionAdminForm(ModelForm):
  class Meta:
    model = Session
    fields = '__all__'
    
class AddSessionForm(ModelForm):
  class Meta:
    model = Session
    exclude = ['is_cancelled','is_closed','players','queue']
    
    widgets = {
      'session_type':forms.Select(attrs={'class':'form-control'}),
      'location':forms.Select(attrs={'class':'form-control'}),
      'duration':forms.Select(attrs={'class':'form-control'}),
      'capacity':forms.TextInput(attrs={'class':'form-control','type':'tel'}),
      'coaches':forms.CheckboxSelectMultiple(attrs={'class':'checkbox-control'}),
      'note':forms.Textarea(attrs={'class':'form-control'}),
    }

  def next_friday():
    t = datetime.now()
    return (t + timedelta(days=(3-t.weekday())%7 +1)).replace(microsecond=0, second=0, minute=0, hour=16)

  def __init__(self, *args, **kwargs):
      super(AddSessionForm, self).__init__(*args, **kwargs)
      self.fields['time'] = forms.SplitDateTimeField(initial=datetime.now().replace(microsecond=0, second=0, minute=0))
      self.fields['time'].widget = forms.SplitDateTimeWidget(
        date_attrs={'type': 'date','class': 'form-control'},
        time_attrs={'type': 'time','class': 'form-control'})


class EditSessionForm(ModelForm):
  class Meta:
    model = Session
    fields = '__all__'
    
    widgets = {
      'session_type':forms.Select(attrs={'class':'form-control'}),
      'location':forms.Select(attrs={'class':'form-control'}),
      'duration':forms.Select(attrs={'class':'form-control'}),
      'capacity':forms.TextInput(attrs={'class':'form-control','type':'tel'}),
      'is_closed': forms.CheckboxInput(attrs={'class':'checkbox-control'}),
      'is_cancelled': forms.CheckboxInput(attrs={'class':'checkbox-control'}),
      'coaches':forms.CheckboxSelectMultiple(attrs={'class':'checkbox-control'}),
      'note':forms.Textarea(attrs={'class':'form-control'}),
      'players':forms.CheckboxSelectMultiple(attrs={'class':'checkbox-control'}),
      'queue':forms.CheckboxSelectMultiple(attrs={'class':'checkbox-control'}),

    }

  def __init__(self, *args, **kwargs):
      super(EditSessionForm, self).__init__(*args, **kwargs)
      self.fields['time'] = forms.SplitDateTimeField()
      self.fields['time'].widget = forms.SplitDateTimeWidget(
        date_attrs={'type': 'date','class': 'form-control'},
        time_attrs={'type': 'time','class': 'form-control'})
