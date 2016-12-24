# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_subject_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(unique=True, max_length=60, verbose_name='slug', blank=True),
        ),
        migrations.AddField(
            model_name='keyword',
            name='slug',
            field=models.SlugField(unique=True, max_length=60, verbose_name='slug', blank=True),
        ),
    ]
