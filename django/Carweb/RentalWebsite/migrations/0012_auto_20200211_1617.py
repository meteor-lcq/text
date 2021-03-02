# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0011_auto_20200211_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stars',
            name='mumber',
            field=models.CharField(max_length=2),
        ),
    ]
