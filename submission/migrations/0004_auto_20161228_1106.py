# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0003_auto_20161228_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='clarity',
            field=models.CharField(default=1, max_length=100, verbose_name='Clarity', choices=[(b'bad', 'Bad'), (b'fragile', 'Fragile'), (b'average', 'Average'), (b'Good', 'Good'), (b'fantastic', 'Fantastic')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='clarity_observation',
            field=models.TextField(max_length=200, null=True, verbose_name='Clarity observation', blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='general',
            field=models.CharField(default=1, max_length=100, verbose_name='General', choices=[(b'bad', 'Bad'), (b'fragile', 'Fragile'), (b'average', 'Average'), (b'Good', 'Good'), (b'fantastic', 'Fantastic')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='general_observation',
            field=models.TextField(max_length=200, null=True, verbose_name='General Observation', blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='knowledge_level_revisor',
            field=models.CharField(default=1, max_length=100, verbose_name='Knowledge Level Revisor', choices=[(b'bad', 'Bad'), (b'fragile', 'Fragile'), (b'average', 'Average'), (b'Good', 'Good'), (b'fantastic', 'Fantastic')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='knowledge_level_revisor_observation',
            field=models.TextField(max_length=200, null=True, verbose_name='Knowledge Level Revisor Observation', blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='originality_observation',
            field=models.TextField(max_length=200, null=True, verbose_name='Originality observation', blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='relevance',
            field=models.CharField(default=1, max_length=100, verbose_name='Relevance', choices=[(b'bad', 'Bad'), (b'fragile', 'Fragile'), (b'average', 'Average'), (b'Good', 'Good'), (b'fantastic', 'Fantastic')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='relevance_observation',
            field=models.TextField(max_length=200, null=True, verbose_name='Relevance Observation', blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='technical_merit',
            field=models.CharField(default=1, max_length=100, verbose_name='Technical Merit', choices=[(b'bad', 'Bad'), (b'fragile', 'Fragile'), (b'average', 'Average'), (b'Good', 'Good'), (b'fantastic', 'Fantastic')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='technical_merit_observation',
            field=models.TextField(max_length=200, null=True, verbose_name='Technical Merit observation', blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='text_quality',
            field=models.CharField(default=1, max_length=100, verbose_name='Text Quality', choices=[(b'bad', 'Bad'), (b'fragile', 'Fragile'), (b'average', 'Average'), (b'Good', 'Good'), (b'fantastic', 'Fantastic')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='text_quality_observation',
            field=models.TextField(max_length=200, null=True, verbose_name='Text Quality Observation', blank=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='originality',
            field=models.CharField(max_length=100, verbose_name='Originality', choices=[(b'bad', 'Bad'), (b'fragile', 'Fragile'), (b'average', 'Average'), (b'Good', 'Good'), (b'fantastic', 'Fantastic')]),
        ),
    ]
