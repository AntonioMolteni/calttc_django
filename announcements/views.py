from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
import requests
from facebook import GraphAPI
from announcements.models import Announcement
from .forms import AddAnnouncementForm, EditAnnouncementForm

@login_required
@staff_member_required
def add_announcement(request):
    page_title = 'Add Announcement'
    submitted = False
    if request.method == "POST":
        form = AddAnnouncementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddAnnouncementForm
        if "submitted" in request.GET:
            submitted = True
    return render(request, 'announcement/add_announcement.html', 
        {
            'page_title': page_title,
            'form': form,
            'submitted': submitted} )


@login_required
@staff_member_required
def edit_announcement(request, announcement_id):
    page_title = "Edit Announcement"
    announcement= Announcement.objects.get(pk=announcement_id)
    form = EditAnnouncementForm(request.POST or None, instance=announcement)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'announcement/edit_announcement.html',
        {
            'page_title': page_title,
            'announcement':announcement,
            'form': form
            })
    
@login_required
@staff_member_required
def delete_announcement(request, announcement_id):
    announcement = Announcement.objects.get(pk=announcement_id)
    announcement.delete()
    return redirect('home')

@login_required
@staff_member_required
def discord_announcement(request):
    # Tutuorial https://www.youtube.com/watch?v=DArlLAq56Mo
    payload = {
        'content': 'test'
    }
    header = {
        'authorization' : 'OTk0NjQ0ODg3NTYxNTc2NDQ4.GmikGc.yTtklkmlTmhTvuL5qkDtXN5-IJMA2X6ta7mFM8'
    }
    r = requests.post('https://discord.com/api/v9/channels/1051992533842010132/messages', data=payload, headers=header)

        