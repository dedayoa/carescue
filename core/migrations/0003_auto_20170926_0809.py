# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170923_0334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='querysession',
            name='session_id',
            field=models.CharField(max_length=255),
        ),
    ]