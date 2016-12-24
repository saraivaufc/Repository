# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_auto_20161223_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='issue_date',
            field=models.DateField(verbose_name='Issue Date'),
        ),
    ]
