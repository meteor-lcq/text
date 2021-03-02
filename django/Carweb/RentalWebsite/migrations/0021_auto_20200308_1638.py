# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0020_auto_20200304_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='o_time',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='send_driver',
            name='sd_num',
            field=models.IntegerField(max_length=2, default=0),
        ),
    ]
