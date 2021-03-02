# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0022_auto_20200308_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='o_day',
            field=models.IntegerField(max_length=3),
        ),
    ]
