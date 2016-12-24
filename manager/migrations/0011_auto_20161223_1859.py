# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_auto_20161223_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='reference',
            field=models.CharField(max_length=1000, verbose_name='Reference'),
        ),
    ]
