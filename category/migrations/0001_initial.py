# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Short descriptive name for this category.', max_length=200)),
                ('subtitle', models.CharField(default=b'', max_length=200, null=True, help_text=b'Some titles may be the same and cause confusion in admin UI. A subtitle makes a distinction.', blank=True)),
                ('slug', models.SlugField(help_text=b'Short descriptive unique name for use in urls.', unique=True, max_length=255)),
                ('parent', models.ForeignKey(blank=True, to='category.Category', null=True)),
                ('sites', models.ManyToManyField(help_text=b'Limits category scope to selected sites.', to='sites.Site', blank=True)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Short descriptive name for this tag.', max_length=200)),
                ('slug', models.SlugField(help_text=b'Short descriptive unique name for use in urls.', unique=True, max_length=255)),
                ('categories', models.ManyToManyField(help_text=b'Categories to which this tag belongs.', to='category.Category', blank=True)),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
    ]
