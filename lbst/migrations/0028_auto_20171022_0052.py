# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-22 00:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lbst', '0027_auto_20171022_0045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='c_food_plots',
            old_name='foodplot_id',
            new_name='food_plot_id',
        ),
    ]
