from django.db import models

from abc import ABCMeta, abstractmethod

#tentar colocar essa classe em todos os models
class BaseModel:
	__metaclass__ = ABCMeta

	@abstractmethod
	def get_search_fields():
		pass

	@abstractmethod
	def get_output_fields():
		pass

	get_search_fields = staticmethod(get_search_fields)
	get_output_fields = staticmethod(get_output_fields)