# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20161223_2322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profile', 'permissions': (('access_manager_admin', 'Access Manager Admin'),)},
        ),
    ]
