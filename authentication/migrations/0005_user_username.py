# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20161229_0649'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, help_text='Please enter you username.', unique=True, max_length=254, verbose_name='Username'),
            preserve_default=False,
        ),
    ]
