# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_unread', models.BooleanField(default=False, verbose_name='Message UnRead')),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last modification')),
            ],
            options={
                'ordering': ['-last_modified'],
                'verbose_name': 'Chat',
                'verbose_name_plural': 'Chats',
            },
        ),
        migrations.CreateModel(
            name='ChatManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('messages_unread', models.IntegerField(default=0, null=True, verbose_name='Messages UnRead', blank=True)),
                ('user', models.OneToOneField(related_name='chat_manager_user', verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-messages_unread'],
                'verbose_name': 'ChatManager',
                'verbose_name_plural': 'ChatsManager',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('read', models.BooleanField(default=False, verbose_name='Read')),
                ('text', models.CharField(max_length=140, null=True, verbose_name='Text', blank=True)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to=b'documents/chat/images/%Y/%m/%d', null=True, verbose_name='Image', blank=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last modification')),
                ('chat', models.ForeignKey(related_name='User', verbose_name='Chat', to='inbox.Chat')),
            ],
            options={
                'ordering': ['-last_modified'],
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.AddField(
            model_name='chat',
            name='chat_manager_receive',
            field=models.ForeignKey(related_name='inbox_manager_response', verbose_name='Chat Manager Receive', to='inbox.ChatManager'),
        ),
        migrations.AddField(
            model_name='chat',
            name='chat_manager_send',
            field=models.ForeignKey(related_name='inbox_manager_request', verbose_name='Chat Manager Send', to='inbox.ChatManager'),
        ),
    ]
