# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0013_auto_20200214_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='o_addr',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
