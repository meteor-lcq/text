# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0024_order_o_vehicle_use'),
    ]

    operations = [
        migrations.AlterField(
            model_name='d_order',
            name='do_time',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
