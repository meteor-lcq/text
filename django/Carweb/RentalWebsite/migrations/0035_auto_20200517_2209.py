# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0034_remove_comment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
