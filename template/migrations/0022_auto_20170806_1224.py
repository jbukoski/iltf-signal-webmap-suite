# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-06 12:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tamaya', '0021_auto_20170806_1223'),
    ]

    operations = [
        migrations.DeleteModel(
            name='forest_bgc',
        ),
        migrations.DeleteModel(
            name='gssurgo_soc',
        ),
    ]