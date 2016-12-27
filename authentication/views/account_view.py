from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserChangeForm, UserCreationForm
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from authentication.models import User
from django.conf import settings

class UserCreate(CreateView):
	template_name = 'authentication/account/register.html'
	model = User
	fields=["first_name", "last_name","email", "password"]
	success_url = reverse_lazy('authentication:login')

	def form_valid(self, form):
		user = form.save(commit=False)
		user.set_password(user.password)
		user.save(group="participant")
		return super(UserCreate, self).form_valid(form)