from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from accounts.models import User
from django.core.mail import send_mail
from .forms import EditDuesLinkForm
from .models import DuesLink

from announcements.models import Announcement

membership_manager_email = "antoniomolteni@berkeley.edu"
president_email = "23zhankanghong@berkeley.edu"

def membership(request):
  page_title = 'Membership'
  announcements = Announcement.objects.filter(on_membership_page=True)
  dues_links = DuesLink.objects.all()

  return render(request, "membership/membership.html",
    {
      'page_title': page_title,
      'announcements': announcements,
      'dues_links': dues_links
    }
  )

@login_required
@staff_member_required
def edit_dues_link(request, dues_link_id):
    page_title = "Edit Dues Link"
    dues_link= DuesLink.objects.get(pk=dues_link_id)
    form = EditDuesLinkForm(request.POST or None, instance=dues_link)
    if form.is_valid():
        form.save()
        return redirect('membership')
    return render(request, 'membership/edit_dues_link.html',
        {
            'page_title': page_title,
            'dues_link': dues_link,
            'form': form
            })


@login_required
def register(request):
	request.user.is_registered = True
	request.user.save() 
	return redirect(reverse('membership') + '#registration')

@login_required
def unregister(request):
	request.user.is_registered = False
	request.user.save()
	return redirect(reverse('membership') + '#registration')

@login_required
@staff_member_required
@user_passes_test(lambda user: user.is_admin)
def approve_membership(request, user_email):
  specified_user = User.objects.get(email=user_email)
  specified_user.is_registered = False
  specified_user.is_member = True
  specified_user.save()
  send_mail(
    "Membership Approved 🏓", 
    "Congratulations " + specified_user.display_name() + "! You are now an official member of Cal Table Tennis.",
    "Cal Table Tennis <notifications@calttc.berkeley.edu>",
    [user_email,]
    )
  return redirect(reverse('manage-users') + '#membership-approval')

@login_required
@staff_member_required
@user_passes_test(lambda user: user.is_admin)
def refuse_membership(request, user_email):
  specified_user = User.objects.get(email=user_email)
  specified_user.is_registered = False
  specified_user.is_member = False
  specified_user.save()
  send_mail(
    "Membership Refused", 
    "Unfortunately, your name was not found on the RSF's list of due paying members. " + 
    " If you suspect a name mismatch or some kind of mistake, you should email our membership manager " + 
    User.objects.get(email=membership_manager_email).display_name() + " (" + membership_manager_email + ").", 
    "Cal Table Tennis <notifications@calttc.berkeley.edu>",
    [user_email,]
    )
  return redirect(reverse('manage-users') + '#membership-approval')
  