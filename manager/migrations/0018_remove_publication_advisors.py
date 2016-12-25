# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0017_publication_community'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='advisors',
        ),
    ]
