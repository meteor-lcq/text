# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0023_auto_20200308_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='o_vehicle_use',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
