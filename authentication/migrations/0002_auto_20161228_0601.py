# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'User', 'permissions': (('list_reviser', 'List Reviser'), ('add_reviser', 'Add Reviser'), ('delete_reviser', 'Delete Reviser'), ('list_administrator', 'List Administrator'), ('add_administrator', 'Add Administrator'), ('delete_administrator', 'Delete Administrator'))},
        ),
    ]
