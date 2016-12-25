# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0016_auto_20161224_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='community',
            field=models.ForeignKey(default=1, verbose_name='Community', to='manager.Community'),
            preserve_default=False,
        ),
    ]
