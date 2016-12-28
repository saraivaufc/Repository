# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0002_submission_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='review_available_in',
        ),
        migrations.AddField(
            model_name='review',
            name='originality',
            field=models.CharField(default=1, max_length=100, verbose_name='originality', choices=[(b'bad', 'Bad'), (b'fragile', 'Fragile'), (b'average', 'Average'), (b'Good', 'Good'), (b'fantastic', 'Fantastic')]),
            preserve_default=False,
        ),
    ]
