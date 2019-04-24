# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2019-04-24 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bmic', '0005_auto_20190424_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='septic_tanks',
            name='inspected',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='septic_tanks',
            name='last_filte',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='septic_tanks',
            name='last_inspe',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='septic_tanks',
            name='lastpumped',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='septic_tanks',
            name='pumped',
            field=models.DateField(null=True),
        ),
    ]
