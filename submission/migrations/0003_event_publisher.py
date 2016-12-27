# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20161226_1744'),
        ('submission', '0002_event_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='publisher',
            field=models.ForeignKey(verbose_name='Publisher', blank=True, to='manager.Publisher', null=True),
        ),
    ]
