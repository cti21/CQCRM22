# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-17 20:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0059_auto_20190917_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='reason',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='宣教失败原因'),
        ),
    ]
