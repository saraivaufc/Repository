# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20161226_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='publisher',
            field=models.ForeignKey(default=1, verbose_name='Publisher', to='manager.Publisher'),
            preserve_default=False,
        ),
    ]
