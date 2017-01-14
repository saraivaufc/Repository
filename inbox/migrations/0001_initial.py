# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='slug', blank=True)),
                ('subject', models.CharField(max_length=140, verbose_name='Subject')),
                ('text', models.TextField(null=True, verbose_name='Text', blank=True)),
                ('file', models.FileField(upload_to=b'documents/message/files/%Y/%m/%d', null=True, verbose_name='File', blank=True)),
                ('message_unread', models.BooleanField(default=False, verbose_name='Message UnRead')),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last modification')),
            ],
            options={
                'ordering': ['-last_modified'],
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='MessageManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('messages_unread', models.IntegerField(default=0, null=True, verbose_name='Messages UnRead', blank=True)),
                ('user', models.OneToOneField(related_name='message_manager_user', verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-messages_unread'],
                'verbose_name': 'MessageManager',
                'verbose_name_plural': 'MessagesManager',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('read', models.BooleanField(default=False, verbose_name='Read')),
                ('text', models.CharField(max_length=140, null=True, verbose_name='Text', blank=True)),
                ('file', models.FileField(upload_to=b'documents/message/files/%Y/%m/%d', null=True, verbose_name='File', blank=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last modification')),
                ('message', models.ForeignKey(related_name='User', verbose_name='Message', to='inbox.Message')),
                ('message_manager', models.ForeignKey(related_name='inbox_message_send', verbose_name='User', to='inbox.MessageManager')),
            ],
            options={
                'ordering': ['last_modified'],
                'verbose_name': 'Reply',
                'verbose_name_plural': 'Replies',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='message_manager_receive',
            field=models.ForeignKey(related_name='inbox_manager_response', verbose_name='To', to='inbox.MessageManager'),
        ),
        migrations.AddField(
            model_name='message',
            name='message_manager_send',
            field=models.ForeignKey(related_name='inbox_manager_request', verbose_name='From', to='inbox.MessageManager'),
        ),
    ]
