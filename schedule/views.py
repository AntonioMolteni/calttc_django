from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from announcements.models import Announcement
from django.forms import modelformset_factory
from django import forms
from .models import TimeSlot
     
def schedule(request):
    page_title = 'Schedule'
    announcements = Announcement.objects.filter(on_schedule_page=True)
    open_play_time_slots = TimeSlot.objects.filter(open_play=True)
    novice_training_time_slots = TimeSlot.objects.filter(novice_training=True)
    intermediate_training_time_slots = TimeSlot.objects.filter(intermediate_training=True)
    advanced_training_time_slots = TimeSlot.objects.filter(advanced_training=True)
    tournaments_time_slots = TimeSlot.objects.filter(tournaments=True)
    return render(request, "schedule.html",
        {
        'page_title': page_title,    
        'announcements': announcements,
        'open_play_time_slots': open_play_time_slots,
        'novice_training_time_slots': novice_training_time_slots,
        'intermediate_training_time_slots': intermediate_training_time_slots,
        'advanced_training_time_slots': advanced_training_time_slots,
        'tournaments_time_slots': tournaments_time_slots,
        }
    )

@staff_member_required
def edit_schedule(request):
    widgets = { "time_slot": forms.TextInput(attrs={'class':'form-control', 'style':'margin-top:0.5rem;'}),
                "day": forms.Select(attrs={'class':'form-control'}),  
                "location": forms.Select(attrs={'class':'form-control'}),
                "availability": forms.Select(attrs={'class':'form-control'}),
                "open_play": forms.CheckboxInput(attrs={'class':'checkbox-control'}),
                "novice_training": forms.CheckboxInput(attrs={'class':'checkbox-control'}),
                "intermediate_training": forms.CheckboxInput(attrs={'class':'checkbox-control'}),
                "advanced_training": forms.CheckboxInput(attrs={'class':'checkbox-control'}),
                "tournaments": forms.CheckboxInput(attrs={'class':'checkbox-control'}),
    }
    all_timeslots = TimeSlot.objects.all()
    initial = [{
        'time_slot': 'New TimeSlot',
        'day': None,
        'location': None,
        'availability' : None,
        'open_play': False,
        'novice_training': False,
        'intermediate_training': False,
        'advanced_training': False,
        'tournaments': False }]

    TimeSlotFormSet = modelformset_factory(TimeSlot, fields=('__all__'), widgets=widgets, extra = 1,)
    if request.method == "POST":
        formset = TimeSlotFormSet(
            request.POST, request.FILES,
            queryset=all_timeslots, initial=initial,
        )

        if formset.is_valid():
            formset.save()
            
            return redirect(reverse('schedule'))
    else:
        formset = TimeSlotFormSet(initial=initial, queryset=all_timeslots,)
        
    return render(request, 'schedule/edit_schedule.html',
        {'formset':formset,
        })