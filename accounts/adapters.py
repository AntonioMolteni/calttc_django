from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class AccountAdapter(DefaultAccountAdapter):
	def save_user(self, request, user, form, commit=False):
		data = form.cleaned_data
		user.email = data['email']
		user.first_name = data['first_name']
		user.last_name = data['last_name']
		if 'password1' in data:
			user.set_password(data['password1'])
		else:
			user.set_unusable_password()
		user.save()
		return user

	def is_open_for_signup(self,request):
		return False

class SocialAccountAdapter(DefaultSocialAccountAdapter):

	def is_open_for_signup(self,request, sociallogin):
		return True
	

