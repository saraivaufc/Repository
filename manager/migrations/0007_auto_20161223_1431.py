# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_auto_20161223_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='reference',
            field=models.TextField(verbose_name='Reference', blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='uri',
            field=models.URLField(max_length=500, verbose_name='URI', blank=True),
        ),
    ]
