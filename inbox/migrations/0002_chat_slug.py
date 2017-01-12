# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='slug',
            field=models.SlugField(unique=True, max_length=100, verbose_name='slug', blank=True),
        ),
    ]
