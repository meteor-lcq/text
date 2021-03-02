# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0028_auto_20200320_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='d_order',
            name='do_drivid',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
