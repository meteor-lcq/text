# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0007_auto_20200209_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, default=1, serialize=False)),
                ('o_user', models.CharField(max_length=20)),
                ('o_vehicle', models.CharField(max_length=30)),
                ('o_send', models.CharField(max_length=20)),
                ('o_time', models.TimeField(auto_now_add=True)),
                ('o_day', models.IntegerField(max_length=2)),
                ('o_money', models.IntegerField(max_length=10)),
            ],
            options={
                'verbose_name_plural': '订单',
            },
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name_plural': '送车员状态'},
        ),
        migrations.RemoveField(
            model_name='level',
            name='lev_num',
        ),
        migrations.RemoveField(
            model_name='state',
            name='num',
        ),
        migrations.AddField(
            model_name='state',
            name='id',
            field=models.AutoField(primary_key=True, default=1, serialize=False),
        ),
        migrations.AddField(
            model_name='vehicle_leasing',
            name='v_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
