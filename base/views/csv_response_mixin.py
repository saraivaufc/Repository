from django.http import JsonResponse
from abc import ABCMeta, abstractmethod

from base.utils import Export

class CSVResponseMixin():
	__metaclass__ = ABCMeta

	def get(self, request, * args, ** kwargs):
		if self.request.GET.get('type') == "csv":
			return Export.to_csv(request, self.get_queryset(), self.model.get_output_fields())
		return super(CSVResponseMixin, self).get(request)

	def get_context_data(self, ** kwargs):
		context = super(CSVResponseMixin, self).get_context_data(** kwargs)
		context['is_csv'] = True
		return context