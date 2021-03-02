# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0029_d_order_do_drivid'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='d_browse',
            field=models.IntegerField(max_length=100, default=0),
        ),
        migrations.AddField(
            model_name='vehicle_leasing',
            name='v_browse',
            field=models.IntegerField(max_length=100, default=0),
        ),
    ]
