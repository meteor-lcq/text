# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0010_auto_20200211_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sex',
            name='sex',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.ForeignKey(default='保密', to='RentalWebsite.Sex'),
        ),
    ]
