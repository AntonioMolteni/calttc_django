
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import NewsletterForm
from .forms import ExportNewsletterCSVForm
from accounts.models import User
from django.core.mail import EmailMultiAlternatives, get_connection
from django.template.loader import get_template, render_to_string
from datetime import timedelta, datetime
import csv
import os
import codecs
from io import StringIO
from django.http import HttpResponse

@login_required
def subscribe(request):
	request.user.newsletter_subscription = True
	request.user.save()
	subscribe_verification = request.GET.get('subscribe_verification')
	next = request.GET.get('next')
	
	if subscribe_verification:
		return redirect(reverse('home') + '?subscribe_verification=True')

	if next:
			return redirect(next+'#newsletter')
	else:
			return redirect('/#newsletter')

@login_required
def unsubscribe(request):
	request.user.newsletter_subscription = False
	request.user.save()
	unsubscribe_verification = request.GET.get('unsubscribe_verification')
	next = request.GET.get('next')
	
	if unsubscribe_verification:
		return redirect(reverse('home') + '?unsubscribe_verification=True')

	if next:
			return redirect(next + '#newsletter' )
	else:
			return redirect('/#newsletter')

def unsubscribe_external(request):
	logout(request)
	return redirect(reverse('unsubscribe') + '?unsubscribe_verification=True')

def subscribe_external(request):
	logout(request)
	return redirect(reverse('subscribe') + '?subscribe_verification=True')

def export_newsletter_csv(request): 
	page_title = 'Export Newsletter CSV'
	if request.method == 'POST':
		form = ExportNewsletterCSVForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['recipients'] == 'OU':
				recipients = User.objects.all().filter(is_active=True).filter(newsletter_subscription = True)
			elif form.cleaned_data['recipients'] == 'OM':
				recipients = User.objects.all().filter(is_active=True).filter(newsletter_subscription = True).filter(is_member = True)
			elif form.cleaned_data['recipients'] == 'AM':
				recipients = User.objects.all().filter(is_active=True).filter(is_member = True)
			else:
				recipients = None
			recipient_list = recipients.values_list('email', flat = True)
		
			response = HttpResponse(
				content_type='text/csv',
				headers={'Content-Disposition': 'attachment; filename="newsletter_emails.csv"'},
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
		form = ExportNewsletterCSVForm()

	return render(request, 'newsletter/export_newsletter.html', 
		{ 'page_title': page_title,
			'form': form
			})

@login_required
@staff_member_required
def compose_newsletter(request):
	page_title = 'Compose Newsletter'
	if request.method == 'POST':
		form = NewsletterForm(request.POST, request.FILES)
		if form.is_valid():
			newsletter = form.save()
			is_list = False
			if newsletter.recipients == 'OU':
				recipients = User.objects.all().filter(is_active=True).filter(newsletter_subscription = True)
			elif newsletter.recipients == 'OM':
				recipients = User.objects.all().filter(is_active=True).filter(newsletter_subscription = True).filter(is_member = True)
			elif newsletter.recipients == 'AM':
				recipients = User.objects.all().filter(is_active=True).filter(is_member = True)
			elif newsletter.recipients == 'TU':
				recipients = None
				is_list = True
				recipient_list = [newsletter.test_user_email,]
			elif newsletter.recipients == 'LI':
				recipients = None
				is_list = True
				file = newsletter.gmail_csv
				reader = csv.DictReader(codecs.iterdecode(file, 'utf-8'))
				recipient_list=[]
				for row in reader:
					recipient_list.append(row['E-mail 1 - Value'])
			else:
				recipients = None
				is_list = True
				recipient_list = []
			if not is_list:
				recipient_list = recipients.values_list('email', flat = True)
		
			# Get Template
			content = newsletter.content
			image = "https://calttc.berkeley.edu/media/" + str(newsletter.image)
			unsubscribe_link = newsletter.unsubscribe_link

			unsubscribe_url = request.build_absolute_uri(reverse('unsubscribe-external'))
			email_context = {
				'content': content,
				'image': image,
				'unsubscribe_link': unsubscribe_link,
				'unsubscribe_url': unsubscribe_url,
				'email': None
			}
			# Static Values for Message Object
			subject = form.cleaned_data['subject']
			from_email = 'Cal Table Tennis <notifications@calttc.berkeley.edu>'
			
			connection = get_connection() # uses SMTP server specified in settings.py
			connection.open()

			for recipient in recipient_list:
				email_context['email'] = recipient

				# Values for Message Object
				text_content = render_to_string('newsletter/email.html', email_context)
				
				# Values for HTML Alternative
				html_template = get_template('newsletter/email.html')
				html_content = html_template.render(email_context)

				# Create Message Object
				msg = EmailMultiAlternatives(subject, text_content, from_email, [recipient])
				msg.attach_alternative(html_content, "text/html")
				
				# Send Message
				try:
					msg.send()
				except:
					print(recipient + ": failed")

			connection.close()

			return redirect(reverse('home'))
	else:
		t = datetime.now()
		week_of_monday =  (t + timedelta(days=-((1+ t.weekday()) % 7 ) + 1))
		month_day_string = week_of_monday.strftime("%m/%d")
		default_subject= "CalTTC Newsletter - Week of " + month_day_string + " 🏓"
		form = NewsletterForm(initial={'subject':default_subject})

	return render(request, 'newsletter/compose_newsletter.html', 
		{ 'page_title': page_title,
			'form': form
			})
