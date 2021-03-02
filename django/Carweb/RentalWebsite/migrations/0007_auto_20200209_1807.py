# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0006_auto_20200206_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('num', models.CharField(primary_key=True, max_length=1, serialize=False)),
                ('state', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='send_driver',
            name='sd_state',
            field=models.ForeignKey(null=True, to='RentalWebsite.State'),
        ),
    ]
