# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0017_auto_20200229_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='D_order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('do_user', models.CharField(max_length=20)),
                ('do_driver', models.CharField(max_length=20)),
                ('do_time', models.TimeField(auto_now_add=True)),
                ('do_money', models.IntegerField(max_length=10)),
            ],
            options={
                'verbose_name_plural': '代驾订单',
            },
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': '租车订单'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name_plural': '司机状态'},
        ),
        migrations.RemoveField(
            model_name='send_driver',
            name='sd_state',
        ),
        migrations.AddField(
            model_name='driver',
            name='d_state',
            field=models.ForeignKey(null=True, to='RentalWebsite.State'),
        ),
        migrations.AddField(
            model_name='send_driver',
            name='sd_num',
            field=models.CharField(max_length=1, default=0),
        ),
    ]
