# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20161227_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='uri',
            field=models.URLField(max_length=500, verbose_name='URI', blank=True),
        ),
    ]
