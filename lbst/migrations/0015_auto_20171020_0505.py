# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-20 05:05
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lbst', '0014_auto_20171020_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counties',
            name='geom',
            field=django.contrib.gis.db.models.fields.PolygonField(srid=4326),
        ),
    ]