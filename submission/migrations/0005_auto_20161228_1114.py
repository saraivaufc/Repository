# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0004_auto_20161228_1106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submission',
            options={'verbose_name': 'Submission', 'verbose_name_plural': 'Submission', 'permissions': (('list_submission_to_review', 'List Submission To  Review'),)},
        ),
    ]
