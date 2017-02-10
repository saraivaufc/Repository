# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-18 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_remove_community_acronym'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='abstract',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='language',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='other_abstract',
        ),
        migrations.AddField(
            model_name='publication',
            name='principal_abstract',
            field=models.TextField(blank=True, null=True, verbose_name='Principal Abstract'),
        ),
        migrations.AddField(
            model_name='publication',
            name='principal_keywords',
            field=models.ManyToManyField(related_name='principal_keywords', to='manager.Keyword', verbose_name='Principal Keywords'),
        ),
        migrations.AddField(
            model_name='publication',
            name='principal_language',
            field=models.CharField(choices=[('pt_BR', 'Brazilian Portuguese'), ('en', 'English'), ('es', 'Spanish')], default=1, max_length=100, verbose_name='Principal Language'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publication',
            name='secondary_abstract',
            field=models.TextField(blank=True, null=True, verbose_name='Secondary Abstract'),
        ),
        migrations.AddField(
            model_name='publication',
            name='secondary_keywords',
            field=models.ManyToManyField(related_name='secondary_keywords', to='manager.Keyword', verbose_name='Secondary Keywords'),
        ),
        migrations.AddField(
            model_name='publication',
            name='secondary_language',
            field=models.CharField(choices=[('pt_BR', 'Brazilian Portuguese'), ('en', 'English'), ('es', 'Spanish')], default=1, max_length=100, verbose_name='Secondary Language'),
            preserve_default=False,
        ),
    ]