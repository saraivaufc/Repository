# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0004_message_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='user',
            new_name='chat_manager',
        ),
    ]
