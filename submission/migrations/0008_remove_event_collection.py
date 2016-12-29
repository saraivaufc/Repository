# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0007_event_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='collection',
        ),
    ]
