# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-06 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tamaya', '0015_auto_20170806_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='forest_agc',
            name='name',
            field=models.TextField(default='agc'),
        ),
    ]