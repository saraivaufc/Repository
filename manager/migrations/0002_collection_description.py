# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='description',
            field=models.TextField(default=1, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
