# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20161223_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=60, verbose_name='slug', blank=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')),
            ],
            options={
                'ordering': ['registration_date'],
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publishers',
            },
        ),
        migrations.RenameField(
            model_name='publication',
            old_name='subjects',
            new_name='subject',
        ),
        migrations.AddField(
            model_name='publication',
            name='address',
            field=models.CharField(default=1, max_length=100, verbose_name='Address'),
            preserve_default=False,
        ),
    ]
