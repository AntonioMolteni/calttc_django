from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import User
from django.contrib.admin.views.decorators import staff_member_required
from .models import User
from django.forms import CheckboxInput, TextInput, modelformset_factory
from accounts.forms import AccountChangeForm
from team.forms import ProfileForm
from .forms import ExportEmailCSVForm
import csv
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta


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
    if User.is_superuser:
        officers = User.objects.filter(is_staff = True)
    else:
        officers = None

    users = User.objects.query_last_login_within_8_months()
    

    # Formset for multiple forms
    widgets={
        "is_member": CheckboxInput(attrs={'class':'checkbox-control', 'tabindex':'-1'},),
        "is_staff": CheckboxInput(attrs={'class':'checkbox-control', 'tabindex':'-1'},),
        "is_admin": CheckboxInput(attrs={'class':'checkbox-control', 'tabindex':'-1'},),
        "rating": TextInput(attrs={'class':'form-control rating','type':'tel'},),
        }
    if not request.user.is_admin:
        widgets['is_member']= CheckboxInput(attrs={'class':'checkbox-control readonly', 'tabindex':'-1'},)
   
    ManageUsersFormSet = modelformset_factory(User, fields=('is_member','is_staff','is_admin','rating'),
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
        'officers':officers,
        'formset': formset }
    )



@login_required
@staff_member_required
def export_email_csv(request): 
    page_title = 'Export Email CSV'
    if request.method == 'POST':
        form = ExportEmailCSVForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['recipients'] == 'U':
                recipients = User.objects.all().filter(is_active=True)
            elif form.cleaned_data['recipients'] == 'M':
                recipients = User.objects.all().filter(is_active=True).filter(is_member = True)
            else:
                recipients = None
 
            field = form.fields['recipients']
            data = form.cleaned_data['recipients'] 
            if isinstance(data, (list, tuple)): 
                # for multi-selects 
                friendly_name = [x[1] for x in field.choices if x[0] in data] 
            else: 
                friendly_name = [x[1] for x in field.choices if x[0] == data] 

            response = HttpResponse(
                content_type='text/csv',
				headers={'Content-Disposition': f'attachment; filename="{friendly_name[0]}_emails.csv"'}
				)
            writer = csv.writer(response)
            writer.writerow(['Name',	'Given Name',	'Additional Name',	'Family Name',	'Yomi Name',	'Given Name Yomi',	'Additional Name Yomi',	'Family Name Yomi',	'Name Prefix',	'Name Suffix',	'Initials',	'Nickname',	'Short Name',	'Maiden Name',	'Birthday',	'Gender',	'Location',	'Billing Information', 'Directory Server',	'Mileage',	'Occupation',	'Hobby',	'Sensitivity', 'Priority',	'Subject',	'Notes',	'Language',	'Photo',	'Group Membership','E-mail 1 - Type',	'E-mail 1 - Value',	'E-mail 2 - Type',	'E-mail 2 - Value'])
            for recipient in recipients:
                user_list = []
                user_list.append(recipient.display_name())
                user_list.append(recipient.first_name)
                user_list.append('')
                user_list.append(recipient.last_name)
                for i in range(24):
                    user_list.append('')
                user_list.append('Newsletter ::: * myContacts')
                user_list.append('* Other')
                user_list.append(recipient.email)
                writer.writerow(user_list)
            return response
    else:
        form = ExportEmailCSVForm()

    return render(request, 'accounts/export_emails.html', 
        { 'page_title': page_title,
            'form': form
            })