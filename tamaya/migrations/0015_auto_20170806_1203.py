# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-06 12:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tamaya', '0014_auto_20170806_1202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forest_agc',
            old_name='raster_id',
            new_name='agc_id',
        ),
    ]
