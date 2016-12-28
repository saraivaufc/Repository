# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20161226_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='uri',
            field=models.URLField(verbose_name='URI', max_length=500, editable=False, blank=True),
        ),
    ]
