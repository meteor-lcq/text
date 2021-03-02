# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0012_auto_20200211_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle_leasing',
            name='v_tag',
        ),
        migrations.AlterField(
            model_name='vehicle_leasing',
            name='v_type',
            field=models.ForeignKey(to='RentalWebsite.Tag'),
        ),
    ]
