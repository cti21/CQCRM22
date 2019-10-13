# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-09-14 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0047_client_from_client_type_jinjizheng'),
    ]

    operations = [
        migrations.CreateModel(
            name='client_register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_type', models.SmallIntegerField(blank=True, default=1, null=True, verbose_name='客户类型')),
                ('registerdate', models.DateField(blank=True, null=True, verbose_name='登记日期')),
                ('lastyuejing', models.DateField(blank=True, null=True, verbose_name='末次月经')),
                ('yunci', models.IntegerField(blank=True, default=0, null=True, verbose_name='孕次')),
                ('chanci', models.IntegerField(blank=True, default=0, null=True, verbose_name='产次')),
                ('taishu', models.SmallIntegerField(blank=True, default=1, null=True, verbose_name='胎数')),
                ('height', models.FloatField(blank=True, default=0, null=True, verbose_name='身高cm')),
                ('preweight', models.FloatField(blank=True, default=0, null=True, verbose_name='孕前体重kg')),
                ('preBMI', models.FloatField(blank=True, default=0, null=True, verbose_name='孕前BMI')),
                ('workqiangdu', models.SmallIntegerField(blank=True, default=1, null=True, verbose_name='工作强度')),
                ('sporttype', models.SmallIntegerField(blank=True, default=1, null=True, verbose_name='运动类型')),
                ('sportttime', models.SmallIntegerField(blank=True, default=1, null=True, verbose_name='运动时间')),
                ('frequency', models.SmallIntegerField(blank=True, default=1, null=True, verbose_name='运动频率')),
                ('healthtype', models.SmallIntegerField(blank=True, default=1, null=True, verbose_name='健康类型')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='家长手机')),
                ('fenmiandate', models.DateField(blank=True, null=True, verbose_name='分娩日期')),
                ('fenmiantype', models.SmallIntegerField(blank=True, default=1, null=True, verbose_name='分娩方式')),
                ('burutype', models.SmallIntegerField(blank=True, default=1, null=True, verbose_name='哺乳方式')),
                ('shoushudate', models.DateField(blank=True, null=True, verbose_name='手术日期')),
                ('shoushuype', models.SmallIntegerField(blank=True, default=1, null=True, verbose_name='手术方式')),
                ('weight', models.FloatField(blank=True, default=0, null=True, verbose_name='当前体重kg')),
                ('BMI', models.FloatField(blank=True, default=0, null=True, verbose_name='当前BMI')),
                ('sourcedept', models.SmallIntegerField(blank=True, default=1, null=True, verbose_name='来源科室id')),
                ('yunzhou', models.IntegerField(blank=True, default=0, null=True, verbose_name='孕周')),
                ('chanhouzhouqi', models.IntegerField(blank=True, default=0, null=True, verbose_name='产后周期')),
                ('ganyutype', models.SmallIntegerField(blank=True, default=1, null=True, verbose_name='干预方式')),
                ('comment', models.CharField(blank=True, max_length=500, null=True, verbose_name='备注')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='education',
            field=models.SmallIntegerField(blank=True, default=1, null=True, verbose_name='学历'),
        ),
        migrations.AddField(
            model_name='client',
            name='nation',
            field=models.SmallIntegerField(blank=True, default=1, null=True, verbose_name='民族'),
        ),
        migrations.AddField(
            model_name='client',
            name='profession',
            field=models.SmallIntegerField(blank=True, default=1, null=True, verbose_name='职业'),
        ),
        migrations.AddField(
            model_name='client_register',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.client', verbose_name='客户id'),
        ),
        migrations.AddField(
            model_name='client_register',
            name='dept',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.dept', verbose_name='登记科室id'),
        ),
    ]