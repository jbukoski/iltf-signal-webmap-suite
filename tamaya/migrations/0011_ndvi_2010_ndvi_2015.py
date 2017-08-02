# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-02 07:09
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamaya', '0010_ndvi_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='ndvi_2010',
            fields=[
                ('raster_id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('raster', django.contrib.gis.db.models.fields.RasterField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='ndvi_2015',
            fields=[
                ('raster_id', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('raster', django.contrib.gis.db.models.fields.RasterField(srid=4326)),
            ],
        ),
    ]
