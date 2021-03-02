# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0019_auto_20200302_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='send_driver',
            name='sd_num',
            field=models.IntegerField(max_length=1, default=0),
        ),
    ]
