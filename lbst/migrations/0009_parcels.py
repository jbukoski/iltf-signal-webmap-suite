# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-20 04:56
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lbst', '0008_delete_parcels'),
    ]

    operations = [
        migrations.CreateModel(
            name='parcels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.FloatField()),
                ('perimeter', models.FloatField()),
                ('biglst_field', models.FloatField()),
                ('biglst_id', models.FloatField()),
                ('pls_town', models.CharField(max_length=4)),
                ('pls_range', models.CharField(max_length=4)),
                ('pls_sec', models.CharField(max_length=2)),
                ('pls_pm', models.CharField(max_length=2)),
                ('lst_owntyp', models.CharField(max_length=1)),
                ('lst_restyp', models.CharField(max_length=1)),
                ('lst_open', models.CharField(max_length=2)),
                ('lst_tractn', models.CharField(max_length=8)),
                ('lst_suffix', models.CharField(max_length=3)),
                ('lst_mtract', models.CharField(max_length=8)),
                ('lst_msuffi', models.CharField(max_length=3)),
                ('lst_lot', models.CharField(max_length=3)),
                ('lst_area', models.FloatField()),
                ('lst_sym', models.IntegerField()),
                ('acres', models.BigIntegerField()),
                ('owntype', models.FloatField()),
                ('owner', models.FloatField()),
                ('own', models.FloatField()),
                ('num', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]