# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20161223_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='publisher',
            field=models.ForeignKey(default=1, verbose_name='Publisher', to='manager.Publisher'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publication',
            name='collection',
            field=models.ForeignKey(verbose_name='Collection', to='manager.Collection'),
        ),
    ]
