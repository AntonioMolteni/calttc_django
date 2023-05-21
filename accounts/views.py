from datetime import datetime, timedelta
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.contrib.admin.views.decorators import staff_member_required
from .models import User
from django.forms import CheckboxInput, TextInput, modelformset_factory
from accounts.forms import AccountChangeForm
from team.forms import ProfileForm


def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    auth_logout(request)
    next = request.GET.get('next')
    if next:
        return redirect(next)
    else:
        return redirect('/')

@login_required
def settings(request):
    page_title = 'Settings'
    profile_instance = request.user.get_profile()
    if request.method == "POST":
        form = AccountChangeForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES or None, instance=profile_instance)
        
        print(profile_form.is_valid())
        print(profile_form.errors)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            
            
            next = request.GET.get('next')
            if next:
                return redirect(next)
            else:
                return redirect('/')
    else:
        form = AccountChangeForm(instance=request.user)
        profile_form = ProfileForm(instance=profile_instance)

 
    return render(request, 'accounts/settings.html',
        {   'page_title': page_title,
            'form': form,
            'profile_instance': profile_instance,
            "profile_form": profile_form
            })

def privacy_policy(request):
    page_title = 'Privacy Policy'
    return render(request, 'accounts/privacy_policy.html',
    {
        'page_title': page_title,
    })

@login_required
@staff_member_required
def manage_users(request):
    page_title = 'Manage Users'

    # Queries
    registered_users = User.objects.filter(is_registered = True)
    members = User.objects.filter(is_member = True)
    users = User.objects.all()
    

    # Formset for multiple forms
    widgets={
        "is_member": CheckboxInput(attrs={'class':'checkbox-control', 'tabindex':'-1'},),
        "newsletter_subscription": CheckboxInput(attrs={'class':'checkbox-control', 'tabindex':'-1'},),
        "rating": TextInput(attrs={'class':'form-control rating','type':'tel'},),
        }
    if not request.user.is_admin:
        widgets['is_member']= CheckboxInput(attrs={'class':'checkbox-control readonly', 'tabindex':'-1'},)
        widgets['newsletter_subscription']= CheckboxInput(attrs={'class':'readonly', 'tabindex':'-1',},)
   
    ManageUsersFormSet = modelformset_factory(User, fields=('is_member','newsletter_subscription','rating'),
        extra = 0, widgets=widgets
        )

    # Form Submission
    if request.method == "POST":
        formset = ManageUsersFormSet(
        request.POST, request.FILES,
        queryset=users,
        )
        if formset.is_valid():
            formset.save()
            next = request.GET.get('next')
            if next:
                return redirect(next)
            else:
                return redirect('/')
    else:
        formset = ManageUsersFormSet(queryset=users)
 
    return render(request, "accounts/manage_users.html",
    { 
        'page_title': page_title,
        'registered_users': registered_users,
        'members': members,
        'formset': formset}
    )
