# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0007_auto_20170112_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='text',
            field=models.CharField(max_length=140, null=True, verbose_name='Text', blank=True),
        ),
    ]
