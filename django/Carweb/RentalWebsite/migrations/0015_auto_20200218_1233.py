# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0014_order_o_addr'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='d_addr',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AddField(
            model_name='send_driver',
            name='sd_addr',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='o_addr',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
