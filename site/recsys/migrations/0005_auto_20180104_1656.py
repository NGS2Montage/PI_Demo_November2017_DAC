# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-04 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recsys', '0004_auto_20180104_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citation',
            name='author',
        ),
        migrations.AddField(
            model_name='citation',
            name='author',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
