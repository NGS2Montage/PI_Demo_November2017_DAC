# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-02 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recsys', '0018_paper_citation_only'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoCitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='paper',
            name='fetched_co_citations',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cocitation',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recsys.Paper'),
        ),
        migrations.AddField(
            model_name='cocitation',
            name='with_paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='with_paper', to='recsys.Paper'),
        ),
    ]
