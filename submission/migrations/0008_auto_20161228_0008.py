# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0007_auto_20161227_0727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=500, verbose_name='Slug', blank=True)),
                ('review_available_in', models.BooleanField(default=False, verbose_name='Review Available')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')),
            ],
        ),
        migrations.AlterModelOptions(
            name='submission',
            options={'verbose_name': 'Submission', 'verbose_name_plural': 'Submission', 'permissions': (('list_all_submissions', 'List all submissions'), ('list_reviser', 'List Reviser'), ('add_reviser', 'Add Reviser'), ('delete_reviser', 'Delete Reviser'))},
        ),
    ]
