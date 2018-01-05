# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 15:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recsys', '0007_paper_citations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citation',
            name='record',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='record', related_query_name='records', to='recsys.Paper'),
        ),
    ]
