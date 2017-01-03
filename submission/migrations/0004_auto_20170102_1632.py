# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0003_auto_20170101_1448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submission',
            options={'verbose_name': 'Submission', 'verbose_name_plural': 'Submission', 'permissions': (('list_submission_to_review', 'List Submission To  Review'), ('submit_final', 'Submit Final'))},
        ),
    ]
