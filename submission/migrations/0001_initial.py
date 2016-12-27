# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=500, verbose_name='Slug', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.FileField(upload_to=b'documents/event/images/%Y/%m/%d', verbose_name='Image')),
                ('typology', models.CharField(max_length=100, verbose_name='Typology', choices=[('conference', 'Conference'), ('workshop', 'Workshop')])),
                ('date', models.DateField(verbose_name='Date')),
                ('submission_1_open', models.DateField(verbose_name='Submission 1 Open')),
                ('submission_1_close', models.DateField(verbose_name='Submission 1 Close')),
                ('review_open', models.DateField(verbose_name='Review Open')),
                ('review_close', models.DateField(verbose_name='Review Close')),
                ('submission_2_open', models.DateField(verbose_name='Submission 2 Open')),
                ('submission_2_close', models.DateField(verbose_name='Submission 2 Close')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')),
                ('collection', models.ForeignKey(verbose_name='Collection', to='manager.Collection')),
                ('community', models.ForeignKey(verbose_name='Community', to='manager.Community')),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'Event',
                'verbose_name_plural': 'Event',
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=500, verbose_name='Slug', blank=True)),
                ('review_available', models.BooleanField(default=False, verbose_name='Review Available')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')),
                ('event', models.ForeignKey(verbose_name='Event', to='submission.Event')),
                ('publication', models.ForeignKey(verbose_name='Publication', blank=True, to='manager.Publication', null=True)),
                ('user', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Submission',
                'verbose_name_plural': 'Submission',
            },
        ),
    ]
