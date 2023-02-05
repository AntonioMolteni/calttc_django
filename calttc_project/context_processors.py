import datetime
from schedule.models import TimeSlot
from images.models import FooterImage
from accounts.models import User
import random


def get_current_year_to_context(request):
	current_datetime = datetime.datetime.now()
	return {
		'current_datetime': current_datetime
	}

def get_schedule_to_context(request):
	open_play_time_slots = TimeSlot.objects.filter(open_play=True)
	return {
		'open_play_time_slots': open_play_time_slots
	}

def get_footer_image_to_context(request):
	all_footer_images = FooterImage.objects.all()
	footer_image = None
	if all_footer_images:
		random_index = random.randint(0, all_footer_images.count() - 1)
		footer_image = all_footer_images[random_index]
	return {
		'footer_image': footer_image
	}
# staff notifications
def get_staff_notifications_to_context(request):
	num_registered_users = User.objects.filter(is_registered = True).count()
	num_checked_in_users = User.objects.filter(is_checked_in = True).count()
	num_users_awaiting_approval = num_registered_users + num_checked_in_users
	num_notifications = num_users_awaiting_approval
	return {
		'num_notifications' : num_notifications
	}
	
# verifies unsubscription from email link
def get_newsletter_verification_to_context(request):
	subscribe_verification = request.GET.get('subscribe_verification')
	unsubscribe_verification = request.GET.get('unsubscribe_verification')


	return {
		'unsubscribe_verification' : unsubscribe_verification,
		'subscribe_verification' : subscribe_verification
	}