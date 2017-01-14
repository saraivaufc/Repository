# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='text',
            field=models.TextField(null=True, verbose_name='Text', blank=True),
        ),
    ]
