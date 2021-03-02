# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0033_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='time',
        ),
    ]
