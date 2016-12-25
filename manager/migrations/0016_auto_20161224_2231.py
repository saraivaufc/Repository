# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0015_auto_20161224_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='community',
        ),
        migrations.AddField(
            model_name='collection',
            name='communities',
            field=models.ManyToManyField(to='manager.Community', verbose_name='Communities'),
        ),
    ]
