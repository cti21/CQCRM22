# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-20 10:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0067_auto_20190920_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treat',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='operate_user', to='backend.userProfile', verbose_name='操作人id'),
        ),
    ]
