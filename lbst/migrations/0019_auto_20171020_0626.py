# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-20 06:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lbst', '0018_auto_20171020_0527'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='boundary',
            options={},
        ),
        migrations.AlterModelOptions(
            name='food_plots',
            options={},
        ),
        migrations.RenameField(
            model_name='food_plots',
            old_name='food_plot_id',
            new_name='id',
        ),
    ]