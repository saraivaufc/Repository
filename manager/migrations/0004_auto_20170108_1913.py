# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20170106_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='community',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='collection',
            field=models.ForeignKey(verbose_name='Collection', to='manager.Collection'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='community',
            field=models.ForeignKey(verbose_name='Community', to='manager.Community'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='uri',
            field=models.URLField(max_length=500, verbose_name='URI'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name='Name'),
        ),
    ]
