# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-11 19:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0030_auto_20190911_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_dict',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.project_dict'),
        ),
        migrations.AlterField(
            model_name='project_dict',
            name='projectid',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, verbose_name='项目id'),
        ),
    ]