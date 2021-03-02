# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0026_auto_20200320_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='d_state',
            field=models.ForeignKey(null=True, to='RentalWebsite.State'),
        ),
    ]
