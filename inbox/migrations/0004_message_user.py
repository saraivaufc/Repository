# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0003_chat_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(related_name='inbox_message_send', default=1, verbose_name='User', to='inbox.ChatManager'),
            preserve_default=False,
        ),
    ]
