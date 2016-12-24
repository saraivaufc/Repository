# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_auto_20161223_2120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-registration_date'], 'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['-registration_date'], 'verbose_name': 'Collection', 'verbose_name_plural': 'Collection'},
        ),
        migrations.AlterModelOptions(
            name='community',
            options={'ordering': ['-registration_date'], 'verbose_name': 'Community', 'verbose_name_plural': 'Communities'},
        ),
        migrations.AlterModelOptions(
            name='keyword',
            options={'ordering': ['-registration_date'], 'verbose_name': 'Keyword', 'verbose_name_plural': 'Keywords'},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['-registration_date'], 'verbose_name': 'Publication', 'verbose_name_plural': 'Publications'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['-registration_date'], 'verbose_name': 'Publisher', 'verbose_name_plural': 'Publishers'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['-registration_date'], 'verbose_name': 'Subject', 'verbose_name_plural': 'Subjects'},
        ),
        migrations.RemoveField(
            model_name='publication',
            name='subject',
        ),
        migrations.AddField(
            model_name='publication',
            name='subjects',
            field=models.ManyToManyField(to='manager.Subject', verbose_name='Subjects'),
        ),
    ]
