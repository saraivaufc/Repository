# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0008_chat_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='file',
            field=versatileimagefield.fields.VersatileImageField(upload_to=b'documents/chat/files/%Y/%m/%d', null=True, verbose_name='File', blank=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='text',
            field=models.TextField(null=True, verbose_name='Text', blank=True),
        ),
    ]
