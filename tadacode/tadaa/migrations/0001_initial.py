# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-31 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=b'', max_length=120)),
                ('status', models.CharField(default=b'Ready', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='CClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cclass', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'CClasses',
            },
        ),
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity', models.CharField(max_length=250)),
                ('cell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tadaa.Cell')),
            ],
            options={
                'verbose_name_plural': 'Entities',
            },
        ),
        migrations.CreateModel(
            name='EntityAnn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('results', models.CharField(default=b'', max_length=500)),
                ('graph_file', models.FileField(default=b'local_models/default.graph', upload_to=b'local_models')),
                ('col_id', models.PositiveIntegerField()),
                ('ann_run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tadaa.AnnRun')),
            ],
        ),
        migrations.AddField(
            model_name='cell',
            name='entity_run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tadaa.EntityAnn'),
        ),
        migrations.AddField(
            model_name='cclass',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tadaa.Entity'),
        ),
    ]
