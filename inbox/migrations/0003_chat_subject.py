# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0002_chat_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='subject',
            field=models.CharField(default=1, max_length=140, verbose_name='Subject'),
            preserve_default=False,
        ),
    ]
