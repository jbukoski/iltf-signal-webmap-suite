# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-20 04:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lbst', '0009_parcels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parcels',
            name='id',
        ),
        migrations.AddField(
            model_name='parcels',
            name='parcel_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]