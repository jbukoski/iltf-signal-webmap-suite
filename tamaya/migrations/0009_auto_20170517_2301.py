# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-17 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamaya', '0008_testraster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testraster',
            name='raster_id',
            field=models.TextField(default=23, primary_key=True, serialize=False),
        ),
    ]