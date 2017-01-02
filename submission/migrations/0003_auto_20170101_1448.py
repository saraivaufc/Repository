# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0002_auto_20170101_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='review_available',
        ),
        migrations.AlterField(
            model_name='review',
            name='clarity',
            field=models.CharField(max_length=100, verbose_name='Clarity', choices=[(b'Bad', 'Bad'), (b'Fragile', 'Fragile'), (b'Average', 'Average'), (b'Good', 'Good'), (b'Fantastic', 'Fantastic')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='general',
            field=models.CharField(max_length=100, verbose_name='General', choices=[(b'Bad', 'Bad'), (b'Fragile', 'Fragile'), (b'Average', 'Average'), (b'Good', 'Good'), (b'Fantastic', 'Fantastic')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='knowledge_level_revisor',
            field=models.CharField(max_length=100, verbose_name='Knowledge Level Revisor', choices=[(b'Bad', 'Bad'), (b'Fragile', 'Fragile'), (b'Average', 'Average'), (b'Good', 'Good'), (b'Fantastic', 'Fantastic')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='originality',
            field=models.CharField(max_length=100, verbose_name='Originality', choices=[(b'Bad', 'Bad'), (b'Fragile', 'Fragile'), (b'Average', 'Average'), (b'Good', 'Good'), (b'Fantastic', 'Fantastic')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='relevance',
            field=models.CharField(max_length=100, verbose_name='Relevance', choices=[(b'Bad', 'Bad'), (b'Fragile', 'Fragile'), (b'Average', 'Average'), (b'Good', 'Good'), (b'Fantastic', 'Fantastic')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='technical_merit',
            field=models.CharField(max_length=100, verbose_name='Technical Merit', choices=[(b'Bad', 'Bad'), (b'Fragile', 'Fragile'), (b'Average', 'Average'), (b'Good', 'Good'), (b'Fantastic', 'Fantastic')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='text_quality',
            field=models.CharField(max_length=100, verbose_name='Text Quality', choices=[(b'Bad', 'Bad'), (b'Fragile', 'Fragile'), (b'Average', 'Average'), (b'Good', 'Good'), (b'Fantastic', 'Fantastic')]),
        ),
    ]
