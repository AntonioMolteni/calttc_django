from django import forms
from django.forms import ModelForm
from .models import Session
from datetime import timedelta, datetime
from accounts.models import User


class SessionAdminForm(ModelForm):
  class Meta:
    model = Session
    fields = '__all__'
    
class AddSessionsForm(ModelForm):
  total_duration = forms.IntegerField(label='Total duration (in minutes)')
  num_sessions = forms.IntegerField(label='Number of sessions')
  start_time = forms.SplitDateTimeField(label='Start time',
    initial=datetime.now().replace(microsecond=0, second=0, minute=0)
    )

  class Meta:
    model = Session
    exclude = ['is_cancelled','is_closed','players','queue','duration','time',]

    widgets = {
      'session_type':forms.Select(attrs={'class':'form-control'}),
      'location':forms.Select(attrs={'class':'form-control'}),
      'capacity':forms.TextInput(attrs={'class':'form-control','type':'tel'}),
      'coaches':forms.CheckboxSelectMultiple(attrs={'class':'checkbox-control'}),
      'note':forms.Textarea(attrs={'class':'form-control'}),
    }

  def __init__(self, *args, **kwargs):
      super(AddSessionsForm, self).__init__(*args, **kwargs)
      self.fields['total_duration'].widget = forms.TextInput(attrs={'class':'form-control','type':'tel'})
      self.fields['num_sessions'].widget = forms.TextInput(attrs={'class':'form-control','type':'tel'})
      self.fields['start_time'].widget = forms.SplitDateTimeWidget(
        date_attrs={'type': 'date','class': 'form-control'},
        time_attrs={'type': 'time','class': 'form-control'})
      
  def clean(self):
      cleaned_data = super().clean()
      total_duration = cleaned_data.get('total_duration')
      num_sessions = cleaned_data.get('num_sessions')

      if total_duration and num_sessions:
          if total_duration % num_sessions != 0:
              self.add_error('total_duration', 'Total duration should be divisible by the number of sessions.')

  def save(self, commit=True):
    sessions = []

    if self.cleaned_data.get('total_duration') and self.cleaned_data.get('num_sessions'):
        total_duration = self.cleaned_data['total_duration']
        num_sessions = self.cleaned_data['num_sessions']
        duration_per_session = total_duration // num_sessions

        for _ in range(num_sessions):
            session = super().save(commit=False)
            session.duration = duration_per_session

            if commit:
                session.save()

            sessions.append(session)

    return sessions
 
  def next_friday():
    t = datetime.now()
    return (t + timedelta(days=(3-t.weekday())%7 +1)).replace(microsecond=0, second=0, minute=0, hour=16)
      


class EditSessionForm(ModelForm):
  
  def get_filtered_players_queryset(self):
      return User.objects.query_last_login_within_8_months

  class Meta:
    model = Session
    fields = '__all__'
    labels = {
      "duration": "Duration (in minutes)"
    }

    widgets = {
      'session_type':forms.Select(attrs={'class':'form-control'}),
      'location':forms.Select(attrs={'class':'form-control'}),
      'duration':forms.TextInput(attrs={'class':'form-control','type':'tel'}),
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
      self.fields['players'].queryset = User.objects.query_last_login_within_8_months()
      self.fields['queue'].queryset = User.objects.query_last_login_within_8_months()