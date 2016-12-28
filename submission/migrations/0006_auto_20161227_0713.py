# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0005_event_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submission',
            options={'verbose_name': 'Submission', 'verbose_name_plural': 'Submission', 'permissions': (('see_all_submissions', 'See all submissions'),)},
        ),
    ]
