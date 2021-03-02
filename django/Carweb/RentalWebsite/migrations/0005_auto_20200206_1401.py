# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0004_auto_20200206_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='d_id',
            field=models.CharField(primary_key=True, max_length=8, serialize=False),
        ),
        migrations.AlterField(
            model_name='send_driver',
            name='sd_id',
            field=models.CharField(primary_key=True, max_length=8, serialize=False),
        ),
    ]
