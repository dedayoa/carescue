# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20170926_0809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='query',
            name='requester',
        ),
        migrations.AddField(
            model_name='querysession',
            name='requester',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Requester'),
            preserve_default=False,
        ),
    ]
