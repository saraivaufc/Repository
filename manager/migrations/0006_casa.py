# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 19:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20170118_2227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('publication_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='manager.Publication')),
                ('nome', models.CharField(max_length=1000, verbose_name=b'Nome')),
            ],
            bases=('manager.publication',),
        ),
    ]
