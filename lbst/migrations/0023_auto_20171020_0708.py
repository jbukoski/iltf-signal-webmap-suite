# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-20 07:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lbst', '0022_auto_20171020_0650'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trees_shrubs',
            options={},
        ),
        migrations.AlterModelOptions(
            name='wetlands',
            options={},
        ),
        migrations.RenameField(
            model_name='trees_shrubs',
            old_name='trees_shrubs_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='wetlands',
            old_name='wetlands_id',
            new_name='id',
        ),
    ]