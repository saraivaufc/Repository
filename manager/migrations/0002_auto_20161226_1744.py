# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='collection',
            field=models.ForeignKey(verbose_name='Collection', blank=True, to='manager.Collection'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='community',
            field=models.ForeignKey(verbose_name='Community', blank=True, to='manager.Community'),
        ),
    ]
