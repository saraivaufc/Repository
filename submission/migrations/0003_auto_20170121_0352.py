# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 06:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20170118_2227'),
        ('submission', '0002_auto_20170117_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='community',
        ),
        migrations.RemoveField(
            model_name='event',
            name='publisher',
        ),
        migrations.AddField(
            model_name='event',
            name='collections',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manager.Collection', verbose_name='Collections'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='communities',
            field=models.ManyToManyField(to='manager.Community', verbose_name='Communities'),
        ),
        migrations.AddField(
            model_name='event',
            name='publishers',
            field=models.ManyToManyField(to='manager.Publisher', verbose_name='Publishers'),
        ),
        migrations.AddField(
            model_name='event',
            name='subjects',
            field=models.ManyToManyField(to='manager.Subject', verbose_name='Subjects'),
        ),
    ]
