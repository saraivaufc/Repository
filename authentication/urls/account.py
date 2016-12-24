from django.conf.urls import include, url
from authentication.views import ProfileCreate
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
	url(r'^login/$', auth_views.login, 
		{'template_name': 'authentication/account/login.html',}, 
		name="login"),
	url(r'^logout/$', auth_views.logout, 
		{'next_page': reverse_lazy("authentication:login")},
		name="logout"),
	url(r'^register/$', ProfileCreate.as_view(), name="register"),
	url(r'^password/reset/$', auth_views.password_reset, 
	 	{'template_name': 'authentication/account/password_reset_form.html',
	 	'post_reset_redirect': '/authentication/password_reset/done/',
	 	'email_template_name': 'authentication/account/password_reset_email.html',},
	 	name='password_reset', 
	 ),

	 url(r'^password_reset/done/$', auth_views.password_reset_done, 
	 	{'template_name': 'authentication/account/password_reset_done.html',},
	 	name='password_reset_done'),

	 url(r'^password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm,
	 	{'template_name': 'authentication/account/password_reset_confirm.html',
	 	'post_reset_redirect': '/authentication/password_reset/complete/',}, 
	 	name='password_reset_confirm'),
	 
	url(r'^password_reset/complete/$', auth_views.password_reset_complete,
	 	{'template_name': 'authentication/account/password_reset_complete.html',},  
	 	name='password_reset_complete'),
]
