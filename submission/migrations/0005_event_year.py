# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0004_auto_20161226_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='year',
            field=models.IntegerField(default=1, verbose_name='Year'),
            preserve_default=False,
        ),
    ]
