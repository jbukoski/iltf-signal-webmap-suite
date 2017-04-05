# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-05 01:40
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='boundary',
            fields=[
                ('boundary_id', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.IntegerField()),
                ('area', models.FloatField()),
                ('perimeter', models.FloatField()),
                ('acres', models.FloatField()),
                ('comments', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Boundary',
            },
        ),
        migrations.CreateModel(
            name='mbls',
            fields=[
                ('mbls_id', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.FloatField()),
                ('perimeter', models.FloatField()),
                ('mbl_field', models.IntegerField()),
                ('mbl_id', models.IntegerField()),
                ('acres', models.FloatField()),
                ('comment', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Master Business Leases',
            },
        ),
        migrations.CreateModel(
            name='roads',
            fields=[
                ('roads_id', models.AutoField(primary_key=True, serialize=False)),
                ('length', models.FloatField()),
                ('rd_id', models.IntegerField(default=9999)),
                ('access', models.CharField(max_length=80)),
                ('name', models.CharField(max_length=80)),
                ('number', models.CharField(max_length=80)),
                ('surface', models.CharField(max_length=80)),
                ('condition', models.CharField(max_length=80)),
                ('rd_class', models.FloatField()),
                ('rd_type', models.CharField(max_length=80)),
                ('sa_id', models.CharField(max_length=80)),
                ('surf_type', models.CharField(max_length=80)),
                ('status', models.CharField(max_length=80)),
                ('hunting', models.CharField(max_length=80)),
                ('comment', models.CharField(max_length=80)),
                ('restrict', models.CharField(max_length=80)),
                ('roadrepair', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Reservation Roads',
            },
        ),
        migrations.CreateModel(
            name='soil_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poly_id', models.BigIntegerField()),
                ('areasymbol', models.CharField(max_length=20)),
                ('spatialver', models.BigIntegerField()),
                ('musym', models.CharField(max_length=6)),
                ('mukey', models.CharField(max_length=30)),
                ('mukey_1', models.CharField(max_length=10)),
                ('tax_class', models.CharField(max_length=254)),
                ('org_matter', models.FloatField()),
                ('composting', models.CharField(max_length=254)),
                ('texture', models.CharField(max_length=254)),
                ('ph_water', models.FloatField()),
                ('bulk_densi', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'Soil Data',
            },
        ),
        migrations.CreateModel(
            name='user_lines',
            fields=[
                ('line_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('comment', models.CharField(max_length=100)),
                ('geom', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'User-defined Lines',
            },
        ),
        migrations.CreateModel(
            name='user_polygons',
            fields=[
                ('polygon_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('comment', models.CharField(max_length=100)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'User-defined Polygons',
            },
        ),
        migrations.CreateModel(
            name='user_pts',
            fields=[
                ('point_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('comment', models.CharField(max_length=100)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
            options={
                'verbose_name_plural': 'User-defined Points',
            },
        ),
    ]
