# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-15 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamaya', '0005_landfire_classes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landfire_classes',
            name='value',
            field=models.TextField(),
        ),
    ]