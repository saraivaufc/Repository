from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.views.i18n import JavaScriptCatalog
from django_js_reverse.views import urls_js
from django.views.decorators.cache import cache_page
from django.utils.translation import ugettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.views.static import serve

import settings

js_info_dict = {
	'app_names': ('Repository.manager',),
}

urlpatterns = i18n_patterns(
	url(r'^$', RedirectView.as_view(url=reverse_lazy('manager:home'), permanent=False), name='home'),
	url(_(r'^manager/'), include('manager.urls', namespace="manager", app_name="manager"), name='manager'),
	url(_(r'^authentication/'), include('authentication.urls', namespace="authentication", app_name="authentication"), name='authentication'),
	url(_(r'^submission/'), include('submission.urls', namespace="submission", app_name="submission"), name='submission'),
	url(_(r'^inbox/'), include('inbox.urls', namespace="inbox", app_name="inbox"), name='inbox'),

	url(_(r'^about$'), TemplateView.as_view(template_name="base/about.html"), name="about"),
	url(_(r'^terms$'), TemplateView.as_view(template_name="base/terms.html"), name="terms"),
	url(_(r'^policies$'), TemplateView.as_view(template_name="base/policies.html"), name="policies"),
	url(_(r'^contact_us$'), TemplateView.as_view(template_name="base/contact_us.html"), name="contact_us"),
		
	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
	url(r'^i18n/', include('django.conf.urls.i18n')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^rosetta/', include('rosetta.urls')),
	url(r'^jsreverse/$', cache_page(3600)(urls_js), name='js_reverse'),
	url(r'^jsi18n/$', JavaScriptCatalog.as_view(packages=['base', 'authentication', 'manager', 'submission', 'inbox', ]), name='javascript-catalog'),
)