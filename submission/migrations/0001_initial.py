# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20161229_0636'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=500, verbose_name='Slug', blank=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='description')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('image', models.FileField(upload_to=b'documents/event/images/%Y/%m/%d', verbose_name='Image')),
                ('typology', models.CharField(max_length=100, verbose_name='Typology', choices=[('conference', 'Conference'), ('workshop', 'Workshop')])),
                ('date', models.DateField(verbose_name='Date')),
                ('submission_1_open', models.DateField(verbose_name='Submission 1 Open')),
                ('submission_1_close', models.DateField(verbose_name='Submission 1 Close')),
                ('review_open', models.DateField(verbose_name='Review Open')),
                ('review_close', models.DateField(verbose_name='Review Close')),
                ('submission_2_open', models.DateField(verbose_name='Submission 2 Open')),
                ('submission_2_close', models.DateField(verbose_name='Submission 2 Close')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')),
                ('community', models.ForeignKey(verbose_name='Community', to='manager.Community')),
                ('publisher', models.ForeignKey(verbose_name='Publisher', to='manager.Publisher')),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'Event',
                'verbose_name_plural': 'Event',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=500, verbose_name='Slug', blank=True)),
                ('originality', models.CharField(max_length=100, verbose_name='Originality', choices=[(b'bad', 'Bad'), (b'fragile', 'Fragile'), (b'average', 'Average'), (b'Good', 'Good'), (b'fantastic', 'Fantastic')])),
                ('originality_observation', models.TextField(null=True, verbose_name='Originality observation', blank=True)),
                ('technical_merit', models.CharField(max_length=100, verbose_name='Technical Merit', choices=[(b'bad', 'Bad'), (b'fragile', 'Fragile'), (b'average', 'Average'), (b'Good', 'Good'), (b'fantastic', 'Fantastic')])),
                ('technical_merit_observation', models.TextField(null=True, verbose_name='Technical Merit observation', blank=True)),
                ('clarity', models.CharField(max_length=100, verbose_name='Clarity', choices=[(b'bad', 'Bad'), (b'fragile', 'Fragile'), (b'average', 'Average'), (b'Good', 'Good'), (b'fantastic', 'Fantastic')])),
                ('clarity_observation', models.TextField(null=True, verbose_name='Clarity observation', blank=True)),
                ('text_quality', models.CharField(max_length=100, verbose_name='Text Quality', choices=[(b'bad', 'Bad'), (b'fragile', 'Fragile'), (b'average', 'Average'), (b'Good', 'Good'), (b'fantastic', 'Fantastic')])),
                ('text_quality_observation', models.TextField(null=True, verbose_name='Text Quality Observation', blank=True)),
                ('relevance', models.CharField(max_length=100, verbose_name='Relevance', choices=[(b'bad', 'Bad'), (b'fragile', 'Fragile'), (b'average', 'Average'), (b'Good', 'Good'), (b'fantastic', 'Fantastic')])),
                ('relevance_observation', models.TextField(null=True, verbose_name='Relevance Observation', blank=True)),
                ('knowledge_level_revisor', models.CharField(max_length=100, verbose_name='Knowledge Level Revisor', choices=[(b'bad', 'Bad'), (b'fragile', 'Fragile'), (b'average', 'Average'), (b'Good', 'Good'), (b'fantastic', 'Fantastic')])),
                ('knowledge_level_revisor_observation', models.TextField(null=True, verbose_name='Knowledge Level Revisor Observation', blank=True)),
                ('general', models.CharField(max_length=100, verbose_name='General', choices=[(b'bad', 'Bad'), (b'fragile', 'Fragile'), (b'average', 'Average'), (b'Good', 'Good'), (b'fantastic', 'Fantastic')])),
                ('general_observation', models.TextField(null=True, verbose_name='General Observation', blank=True)),
                ('review_available_in', models.DateTimeField(auto_now_add=True, verbose_name='Review Available In')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=500, verbose_name='Slug', blank=True)),
                ('review_available', models.BooleanField(default=False, verbose_name='Review Available')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')),
                ('event', models.ForeignKey(verbose_name='Event', to='submission.Event')),
                ('publication', models.ForeignKey(verbose_name='Publication', blank=True, to='manager.Publication', null=True)),
                ('review', models.ForeignKey(verbose_name='Review', blank=True, to='submission.Review', null=True)),
                ('reviser', models.ForeignKey(related_name='Reviser', verbose_name='Reviser', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('user', models.ForeignKey(related_name='User', verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Submission',
                'verbose_name_plural': 'Submission',
                'permissions': (('list_submission_to_review', 'List Submission To  Review'),),
            },
        ),
    ]
