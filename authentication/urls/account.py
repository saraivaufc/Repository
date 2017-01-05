from django.conf.urls import include, url
from authentication.views import UserCreateView, UserDetailView, UserUpdateView, UserDeleteView
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

urlpatterns = [
	url(r'^login/$', auth_views.login, {'template_name': 'authentication/account/login.html',}, name="account_login"),
	url(r'^logout/$', auth_views.logout, {'next_page': reverse_lazy("authentication:account_login")}, name="account_logout"),
	url(r'^register/$', UserCreateView.as_view(), name="account_register"),
	url(r'^(?P<pk>[0-9]+)/detail/$', UserDetailView.as_view(), name="account_detail"),
	url(r'^(?P<pk>[0-9]+)/edit/$', UserUpdateView.as_view(), name="account_update"),
	url(r'^(?P<pk>[0-9]+)/delete/$', UserDeleteView.as_view(), name="account_delete"),

	url(r'^password/reset/$', auth_views.password_reset, 
	 	{'template_name': 'authentication/account/password_reset_form.html',
	 	'post_reset_redirect': '/authentication/password_reset/done/',
	 	'email_template_name': 'authentication/account/password_reset_email.html',},
	 	name='account_password_reset', 
	 ),

	 url(r'^password_reset/done/$', auth_views.password_reset_done, 
	 	{'template_name': 'authentication/account/password_reset_done.html',},
	 	name='account_password_reset_done'),

	 url(r'^password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm,
	 	{'template_name': 'authentication/account/password_reset_confirm.html',
	 	'post_reset_redirect': '/authentication/password_reset/complete/',}, 
	 	name='account_password_reset_confirm'),
	 
	url(r'^password_reset/complete/$', auth_views.password_reset_complete,
	 	{'template_name': 'authentication/account/password_reset_complete.html',},  
	 	name='account_password_reset_complete'),
]
