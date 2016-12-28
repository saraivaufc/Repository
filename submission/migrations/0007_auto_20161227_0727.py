# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('submission', '0006_auto_20161227_0713'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submission',
            options={'verbose_name': 'Submission', 'verbose_name_plural': 'Submission', 'permissions': (('list_all_submissions', 'List all submissions'),)},
        ),
        migrations.AddField(
            model_name='submission',
            name='reviser',
            field=models.ForeignKey(related_name='Reviser', verbose_name='Reviser', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(related_name='User', verbose_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]
