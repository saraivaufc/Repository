# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review_available_in',
        ),
        migrations.RemoveField(
            model_name='review',
            name='slug',
        ),
    ]
