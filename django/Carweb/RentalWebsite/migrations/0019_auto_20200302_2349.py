# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0018_auto_20200301_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle_leasing',
            name='v_price_week',
        ),
        migrations.RemoveField(
            model_name='vehicle_leasing',
            name='v_price_work',
        ),
        migrations.AddField(
            model_name='d_order',
            name='do_day',
            field=models.IntegerField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='d_order',
            name='do_time_to',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='o_time_to',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='vehicle_leasing',
            name='v_price_day',
            field=models.IntegerField(max_length=5, null=True),
        ),
    ]
