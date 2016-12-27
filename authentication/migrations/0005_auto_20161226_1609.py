# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20161226_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, help_text='Please enter you email.', unique=True, max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=1, help_text='Please enter you first name.', max_length=100, verbose_name='First Name '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=1, help_text='Please enter you last name.', max_length=100, verbose_name='Last Name '),
            preserve_default=False,
        ),
    ]
