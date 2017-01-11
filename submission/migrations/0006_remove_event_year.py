# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0005_auto_20170110_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='year',
        ),
    ]
