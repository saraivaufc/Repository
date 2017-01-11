# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0004_auto_20170102_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(upload_to=b'documents/event/images/%Y/%m/%d', verbose_name='Image'),
        ),
    ]
