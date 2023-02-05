from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from accounts.models import User
from django.core.mail import send_mail

from announcements.models import Announcement

membership_manager_email = "antoniomolteni@berkeley.edu"
president_email = "23zhankanghong@berkeley.edu"

def membership(request):
  page_title = 'Membership'
  announcements = Announcement.objects.filter(on_membership_page=True)

  # Remove past drop in status
  for user in User.objects.filter(paid_drop_in_fee = True).exclude(last_drop_in_date = None):
      if datetime.now() > user.last_drop_in_date + timedelta(days=1):
          user.paid_drop_in_fee = False
          user.save()

  return render(request, "membership.html",
    {
      'page_title': page_title,
      'announcements': announcements,
    }
  )


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

# Accounts Page Staff User Approval
@login_required
@staff_member_required
def approve_drop_in(request, user_email):
  specified_user = User.objects.get(email=user_email)
  specified_user.is_checked_in = False
  specified_user.paid_drop_in_fee = True
  specified_user.last_drop_in_date = datetime.now()
  specified_user.save()
  return redirect(reverse('manage-users') + '#drop-in-approval')

@login_required
@staff_member_required
def refuse_drop_in(request, user_email):
  specified_user = User.objects.get(email=user_email)
  specified_user.is_checked_in = False
  specified_user.has_paid = False
  specified_user.save()
  return redirect(reverse('manage-users') + '#drop-in-approval')

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
  