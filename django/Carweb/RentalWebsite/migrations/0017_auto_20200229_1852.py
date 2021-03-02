# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0016_auto_20200227_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle_leasing',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
