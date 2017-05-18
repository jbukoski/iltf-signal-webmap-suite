# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-17 22:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamaya', '0005_auto_20170517_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testraster',
            name='rast_name',
        ),
        migrations.AddField(
            model_name='testraster',
            name='name',
            field=models.TextField(default='tester'),
        ),
        migrations.AddField(
            model_name='testraster',
            name='raster_id',
            field=models.TextField(default=1, primary_key=True, serialize=False),
        ),
    ]