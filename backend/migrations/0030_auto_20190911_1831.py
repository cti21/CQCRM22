# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-11 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0029_auto_20190911_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_dict',
            name='amount',
            field=models.IntegerField(blank=True, null=True, verbose_name='数量'),
        ),
    ]
