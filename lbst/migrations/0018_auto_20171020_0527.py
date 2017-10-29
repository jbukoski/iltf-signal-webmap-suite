# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-20 05:27
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lbst', '0017_auto_20171020_0506'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_purchases',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('objectid', models.BigIntegerField()),
                ('area', models.FloatField()),
                ('perimeter', models.FloatField()),
                ('bigplsc_field', models.BigIntegerField()),
                ('bigplsc_id', models.BigIntegerField()),
                ('sec', models.IntegerField()),
                ('town', models.CharField(max_length=3)),
                ('rng', models.CharField(max_length=3)),
                ('mer', models.IntegerField()),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('remarks', models.CharField(max_length=150)),
                ('purch_name', models.CharField(max_length=50)),
                ('purch_date', models.CharField(max_length=50)),
                ('sect_t_r', models.CharField(max_length=50)),
                ('legal_desc', models.CharField(max_length=250)),
                ('acres_field', models.BigIntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.DeleteModel(
            name='new_parcels',
        ),
    ]