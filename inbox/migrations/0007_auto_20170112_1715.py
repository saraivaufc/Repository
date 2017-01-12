# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0006_auto_20170112_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='image',
        ),
        migrations.AddField(
            model_name='message',
            name='file',
            field=versatileimagefield.fields.VersatileImageField(upload_to=b'documents/chat/files/%Y/%m/%d', null=True, verbose_name='File', blank=True),
        ),
    ]
