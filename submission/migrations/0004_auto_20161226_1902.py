# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0003_event_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='publisher',
            field=models.ForeignKey(default=1, verbose_name='Publisher', to='manager.Publisher'),
            preserve_default=False,
        ),
    ]
