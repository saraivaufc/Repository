# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('reference_name', models.CharField(max_length=200, null=True, verbose_name='Reference name', blank=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')),
            ],
            options={
                'ordering': ['registration_date'],
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=60, verbose_name='slug', blank=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')),
            ],
            options={
                'ordering': ['registration_date'],
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collection',
            },
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('acronym', models.CharField(max_length=100, verbose_name='Acronym')),
                ('slug', models.SlugField(unique=True, max_length=60, verbose_name='slug', blank=True)),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')),
            ],
            options={
                'ordering': ['registration_date'],
                'verbose_name': 'Community',
                'verbose_name_plural': 'Communities',
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')),
            ],
            options={
                'ordering': ['registration_date'],
                'verbose_name': 'Keyword',
                'verbose_name_plural': 'Keywords',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, max_length=60, verbose_name='slug', blank=True)),
                ('typology', models.CharField(max_length=100, verbose_name='Typology', choices=[('article', 'Article'), ('book', 'Book'), ('booklet', 'Booklet'), ('conference', 'Conference'), ('inbook', 'Inbook'), ('incollection', 'Incollection'), ('manual', 'Manual'), ('mastersthesis', 'Masters Thesis')])),
                ('issue_date', models.DateField(verbose_name='Issue Date')),
                ('reference', models.TextField(verbose_name='Reference')),
                ('abstract', models.TextField(verbose_name='Abstract')),
                ('other_abstract', models.TextField(null=True, verbose_name='Other Abstract', blank=True)),
                ('uri', models.URLField(max_length=500, verbose_name='URI')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('language', models.CharField(max_length=100, verbose_name='Language', choices=[('pt_BR', 'Brazilian Portuguese'), ('en', 'English'), ('es', 'Spanish')])),
                ('file', models.FileField(upload_to=b'documents/publication/%Y/%m/%d', verbose_name='File')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')),
                ('advisors', models.ManyToManyField(related_name='Advisors', verbose_name='Advisors', to='manager.Author')),
                ('authors', models.ManyToManyField(related_name='Authors', verbose_name='Authors', to='manager.Author')),
                ('collection', models.ForeignKey(verbose_name='collection', to='manager.Collection')),
                ('keywords', models.ManyToManyField(related_name='Keywords', verbose_name='Keywords', to='manager.Keyword')),
            ],
            options={
                'ordering': ['registration_date'],
                'verbose_name': 'Publication',
                'verbose_name_plural': 'Publications',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('registration_date', models.DateTimeField(auto_now_add=True, verbose_name='Registration Date')),
            ],
            options={
                'ordering': ['registration_date'],
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.AddField(
            model_name='publication',
            name='subjects',
            field=models.ForeignKey(verbose_name='Subject', to='manager.Subject'),
        ),
        migrations.AddField(
            model_name='collection',
            name='community',
            field=models.ForeignKey(verbose_name='Community', to='manager.Community'),
        ),
    ]
