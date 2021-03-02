# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0003_auto_20200206_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='send_driver',
            options={'verbose_name_plural': '送车员'},
        ),
    ]
