# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0007_auto_20170121_1622'),
        ('submission', '0004_auto_20170121_0405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='id',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='publication',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='registration_date',
        ),
        migrations.RemoveField(
            model_name='submission',
            name='slug',
        ),
        migrations.AddField(
            model_name='submission',
            name='publication_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='manager.Publication'),
            preserve_default=False,
        ),
    ]
