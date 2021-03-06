# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-19 01:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('list_participant', 'List Participant'), ('list_reviser', 'List Reviser'), ('add_reviser', 'Add Reviser'), ('change_reviser', 'Change Reviser'), ('delete_reviser', 'Delete Reviser'), ('list_administrator', 'List Administrator'), ('add_administrator', 'Add Administrator'), ('delete_administrator', 'Delete Administrator')), 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
