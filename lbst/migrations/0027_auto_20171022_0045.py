# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-22 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lbst', '0026_auto_20171022_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_food_plots',
            name='foodplot_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='c_native_grasslands',
            name='native_grass_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='c_new_grasslands',
            name='new_grass_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='c_new_treebelt',
            name='new_tree_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='c_old_treebelts',
            name='old_tree_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='c_wetlands',
            name='wetland_id',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
