# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0014_auto_20161224_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='community',
        ),
        migrations.AddField(
            model_name='collection',
            name='community',
            field=models.ManyToManyField(to='manager.Community', verbose_name='Community'),
        ),
    ]
