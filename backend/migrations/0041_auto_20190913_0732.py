# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-13 07:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0040_auto_20190913_0613'),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('sex', models.CharField(blank=True, max_length=10, null=True, verbose_name='性别')),
                ('birthDate', models.DateField(blank=True, null=True, verbose_name='出生日期')),
                ('profession', models.CharField(blank=True, max_length=100, null=True, verbose_name='职称')),
                ('education', models.CharField(blank=True, max_length=100, null=True, verbose_name='学历')),
                ('type', models.CharField(blank=True, max_length=10, null=True, verbose_name='职工类型')),
                ('phone1', models.CharField(blank=True, max_length=50, null=True, verbose_name='电话1')),
                ('phone2', models.CharField(blank=True, max_length=50, null=True, verbose_name='电话2')),
                ('hiredate', models.DateField(blank=True, null=True, verbose_name='入职日期')),
                ('state', models.BooleanField(default=1, verbose_name='入职状态')),
                ('comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='备注')),
                ('hrmdepartment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.HrmDepartment', verbose_name='中心id')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='permission',
            options={'permissions': (('tuitionFee', '带教费'), ('performance_dict', '绩效字典'), ('benefit_dict', '工资福利字典'), ('performance', '中心绩效'), ('benefit', '中心工资福利字典'), ('huiyuan_set', '回院设置'), ('tuition_dict', '带教费类型'), ('project_dict', '项目字典'), ('project', '中心项目'), ('finance_month', '财务月'), ('coo_hospital', '合作医院'), ('dept_dict', '科室字典'), ('post_dict', '岗位字典'), ('dept', '中心科室'), ('organization', '组织机构设置'), ('xlog', '操作日志'), ('userProfile', '员工档案'))},
        ),
    ]
