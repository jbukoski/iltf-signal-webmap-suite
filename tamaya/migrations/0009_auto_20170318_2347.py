# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-18 23:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tamaya', '0008_soil_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='bulk_density',
        ),
        migrations.DeleteModel(
            name='composting',
        ),
        migrations.DeleteModel(
            name='soil_ph',
        ),
        migrations.DeleteModel(
            name='taxonomy',
        ),
    ]