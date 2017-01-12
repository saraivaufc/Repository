# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('inbox', '0009_auto_20170112_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('read', models.BooleanField(default=False, verbose_name='Read')),
                ('text', models.CharField(max_length=140, null=True, verbose_name='Text', blank=True)),
                ('file', models.FileField(upload_to=b'documents/chat/files/%Y/%m/%d', null=True, verbose_name='File', blank=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last modification')),
            ],
            options={
                'ordering': ['last_modified'],
                'verbose_name': 'Reply',
                'verbose_name_plural': 'Replies',
            },
        ),
        migrations.RemoveField(
            model_name='message',
            name='chat',
        ),
        migrations.RemoveField(
            model_name='message',
            name='chat_manager',
        ),
        migrations.AlterField(
            model_name='chat',
            name='file',
            field=models.FileField(upload_to=b'documents/chat/files/%Y/%m/%d', null=True, verbose_name='File', blank=True),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.AddField(
            model_name='reply',
            name='chat',
            field=models.ForeignKey(related_name='User', verbose_name='Chat', to='inbox.Chat'),
        ),
        migrations.AddField(
            model_name='reply',
            name='chat_manager',
            field=models.ForeignKey(related_name='inbox_message_send', verbose_name='User', to='inbox.ChatManager'),
        ),
    ]
