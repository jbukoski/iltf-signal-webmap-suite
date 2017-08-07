# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-07 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamaya', '0023_forest_bgc_gssurgo_soc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landfire_evt',
            name='name',
        ),
        migrations.RemoveField(
            model_name='landfire_evt',
            name='raster_id',
        ),
        migrations.RemoveField(
            model_name='ndvi_2005',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ndvi_2005',
            name='raster_id',
        ),
        migrations.RemoveField(
            model_name='ndvi_2010',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ndvi_2010',
            name='raster_id',
        ),
        migrations.RemoveField(
            model_name='ndvi_2015',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ndvi_2015',
            name='raster_id',
        ),
        migrations.AddField(
            model_name='landfire_evt',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ndvi_2005',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ndvi_2010',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ndvi_2015',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
