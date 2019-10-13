# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-13 05:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0036_auto_20190912_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='huiyuan_set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='备注')),
                ('deptdict', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.dept_dict', verbose_name='科室id')),
            ],
        ),
    ]