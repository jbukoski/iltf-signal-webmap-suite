# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-19 21:07
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamaya', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='soil_ph',
            fields=[
                ('ph_id', models.AutoField(primary_key=True, serialize=False)),
                ('areasymbol', models.CharField(max_length=20)),
                ('spatialver', models.BigIntegerField()),
                ('musym', models.CharField(max_length=6)),
                ('mukey', models.CharField(max_length=30)),
                ('mukey_1', models.CharField(max_length=10)),
                ('phwater', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]
