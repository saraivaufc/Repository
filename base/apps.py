# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class BaseConfig(AppConfig):
	name = 'base'
	verbose_name = _("Base")

	def ready(self):
		pass