# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-13 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0041_auto_20190913_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='state',
            field=models.SmallIntegerField(default=1, verbose_name='入职状态'),
        ),
    ]