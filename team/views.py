from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from announcements.models import Announcement
from django.forms import modelformset_factory
from django import forms

from .forms import ProfileForm
from .models import Profile


 
def team(request):
    page_title = 'Team'
    announcements = Announcement.objects.filter(on_team_page=True)
    executive_profiles = Profile.objects.filter(executive = True).order_by('pk')
    officer_profiles = Profile.objects.filter(officer = True).order_by('user__display_name')
    competitive_team_profiles = Profile.objects.filter(competitive_team = True).exclude(user=None).order_by('-user__rating')
    return render(request, "team/team.html",
        {
        'page_title': page_title,
        'announcements': announcements,
        'executive_profiles': executive_profiles,
        'officer_profiles': officer_profiles,
        'competitive_team_profiles': competitive_team_profiles,
        }
    )

@staff_member_required
def edit_profiles(request):
    widgets = {  
        "profile_picture": forms.ClearableFileInput(attrs={'class':'form-control-file','style':'margin-top:0.5rem; font-size:1rem;'}),
        "user": forms.Select(attrs={'class':'form-control','style':'margin-top:0.5rem;'}),
        "position": forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Title'}),
        "about": forms.Textarea(attrs={'class':'form-control', 'placeholder': 'About', 'style':'height:calc(3*(1.5em + .75rem + 2px)); margin:0.5rem 0;'}),
        "show_rating": forms.CheckboxInput(attrs={'class':'checkbox-control', 'style':'margin-top:0.5rem;'}),
        "executive": forms.CheckboxInput(attrs={'class':'checkbox-control'}),
        "officer": forms.CheckboxInput(attrs={'class':'checkbox-control'}),
        "competitive_team": forms.CheckboxInput(attrs={'class':'checkbox-control'}),           
    }
    all_profiles = Profile.objects.all()
    initial = [{
        'profile_picture': None,
        'user': None,
        'position': None,
        'about': None,
        'show_rating': False,
        'executive': False,
        'officer': False,
        'competitive_team': False,

        }]

    ProfileFormSet = modelformset_factory(Profile, form=ProfileForm, widgets=widgets, extra=1,)
    if request.method == "POST":
        formset = ProfileFormSet(request.POST, request.FILES, queryset=all_profiles, initial=initial,
        )
        if formset.is_valid():
            formset.save()
            return redirect(reverse('team'))
    else:
        formset = ProfileFormSet(queryset=all_profiles, initial=initial)
        
    return render(request, 'team/edit_profiles.html',
        {'formset':formset,
        })