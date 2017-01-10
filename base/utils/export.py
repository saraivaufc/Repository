from __future__ import unicode_literals

from django.http import HttpResponse
from django.core import serializers
from django.utils.translation import ugettext_lazy as _
import csv
import json

class Export:
	def to_serial(request, type, queryset, fields):
		serial= serializers.serialize(type, queryset, fields=fields, use_natural_foreign_keys=True, use_natural_primary_keys=True)
		return serial

	def to_csv(request, queryset, fields):
		response = HttpResponse(content_type='text/csv')
		response['Content-Disposition'] = 'attachment; filename="submissions.csv"'
		writer = csv.writer(response)
		writer.writerow(map(lambda x: x[1], fields))
		serial = Export.to_serial(request, 'json', queryset, dict(fields).keys())
		objects= json.loads(serial)
		for obj in objects:
			values=[]
			for field in map(lambda x: x[0], fields):
				value = obj['fields'][field]
				print type(value)
				#se o campo for uma lista, converta para string
				if type(value) == list:
					value = reduce(lambda x, y: x + ';' + y, value)
				#se o campo for um numero, converta para string
				elif type(value) == int or type(value) == float:
					value = str(value)
				#se o campo estiver vazio, converta para string
				elif type(value) == type(None):
					value = _("Empty")
				value = value.encode('utf8')
				values.append(value)
			writer.writerow(values)
		return response


	to_serial = staticmethod(to_serial)
	to_csv = staticmethod(to_csv)