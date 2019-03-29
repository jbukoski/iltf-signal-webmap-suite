# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-03-29 00:05
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('docfile', models.FileField(upload_to='ssmt/uploaded')),
            ],
        ),
        migrations.CreateModel(
            name='parcels',
            fields=[
                ('objectid', models.IntegerField()),
                ('joined', models.IntegerField()),
                ('planid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('type', models.IntegerField()),
                ('statedarea', models.CharField(max_length=50)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('category', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('wateracces', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=5)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]