from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse, HttpResponse
from django.views.generic import View

class ReverseView(View):
	def get(self, request, * args, ** kwargs):
		self.request.GET = dict(self.request.GET.copy())
		for key, value in self.request.GET.items():
			self.request.GET[key] = value[0] if type(value)==type([]) and len(value) == 1 else value
		app_name = kwargs['app_name'] if 'app_name' in kwargs.keys() else None
		url_name = kwargs['url_name']
		if app_name:
			self.url = reverse_lazy(app_name + ':' + url_name, kwargs=dict(self.request.GET))
		else:
			self.url = reverse_lazy(url_name, args)
		try:
			response = JsonResponse({'url': str(self.url)})
		except Exception, e:
			response = HttpResponse(e);
			response.status_code = 500
		return response