# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-04-24 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmic', '0006_auto_20190424_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drainfields',
            name='date_const',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='drainfields',
            name='repaired',
            field=models.DateField(null=True),
        ),
    ]