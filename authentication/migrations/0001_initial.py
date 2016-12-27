# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('first_name', models.CharField(help_text='Please enter you first name.', max_length=100, null=True, verbose_name='First Name ')),
                ('last_name', models.CharField(help_text='Please enter you last name.', max_length=100, null=True, verbose_name='Last Name ')),
                ('email', models.EmailField(null=True, max_length=254, blank=True, help_text='Please enter you email.', unique=True, verbose_name='Email')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
            ],
            options={
                'swappable': 'AUTH_USER_MODEL',
                'db_table': 'auth_user',
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profile',
            },
        ),
    ]
