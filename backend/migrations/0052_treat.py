# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-14 22:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0051_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='treat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isacquire', models.SmallIntegerField(default=0, verbose_name='是否收单')),
                ('times', models.IntegerField(default=0, verbose_name='开单次数')),
                ('residue', models.IntegerField(default=0, verbose_name='剩余次数')),
                ('amount', models.IntegerField(default=0, verbose_name='今天治疗次数')),
                ('operatedate', models.DateTimeField(blank=True, null=True, verbose_name='操作日期')),
                ('comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='备注')),
                ('adduser', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='adduser_treat', to=settings.AUTH_USER_MODEL, verbose_name='开单人id')),
                ('client', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.client', verbose_name='客户id')),
                ('hrmdepartment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.HrmDepartment', verbose_name='中心id')),
                ('operator', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='operate_user', to=settings.AUTH_USER_MODEL, verbose_name='操作人id')),
                ('order', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.order', verbose_name='订单id')),
                ('orderdept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderdept_treat', to='backend.dept', verbose_name='开单科室id')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.treat')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.project', verbose_name='开单项目id')),
                ('treatdept', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='treat_dept', to='backend.dept', verbose_name='治疗科室id')),
            ],
        ),
    ]
