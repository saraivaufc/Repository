# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0005_auto_20170112_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='chat_manager_receive',
            field=models.ForeignKey(related_name='inbox_manager_response', verbose_name='To', to='inbox.ChatManager'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='chat_manager_send',
            field=models.ForeignKey(related_name='inbox_manager_request', verbose_name='From', to='inbox.ChatManager'),
        ),
    ]
