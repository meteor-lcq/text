# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0025_auto_20200320_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='d_state',
            field=models.CharField(max_length=10, default='在岗'),
        ),
    ]
