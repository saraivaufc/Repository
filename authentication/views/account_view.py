from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserChangeForm, UserCreationForm
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from authentication.models import Profile

class ProfileCreate(CreateView):
	template_name = 'authentication/account/register.html'
	model = Profile
	fields=["first_name", "last_name","username","email", "password"]
	success_url = reverse_lazy('authentication:login')

	def form_valid(self, form):
		profile = form.save()
		print profile.email
		return super(ProfileCreate, self).form_valid(form)