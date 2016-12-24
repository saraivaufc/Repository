# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0013_auto_20161223_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='typology',
            field=models.CharField(max_length=100, verbose_name='Typology', choices=[('article', 'Article'), ('book', 'Book'), ('booklet', 'Booklet'), ('conference', 'Conference'), ('inbook', 'Inbook'), ('incollection', 'Incollection'), ('manual', 'Manual'), ('mastersthesis', 'Masters Thesis'), ('monography', 'Monography'), ('dissertation', 'Dissertation'), ('abstract', 'Abstract')]),
        ),
    ]
