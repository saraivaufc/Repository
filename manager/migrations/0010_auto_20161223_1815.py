# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_auto_20161223_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='advisors',
            field=models.ManyToManyField(related_name='Advisors', null=True, verbose_name='Advisors', to='manager.Author', blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='publisher',
            field=models.ForeignKey(verbose_name='Publisher', blank=True, to='manager.Publisher', null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='reference',
            field=models.CharField(max_length=1000, verbose_name='Reference', blank=True),
        ),
    ]
