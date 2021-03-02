# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0005_auto_20200206_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='d_id',
        ),
        migrations.RemoveField(
            model_name='send_driver',
            name='sd_id',
        ),
        migrations.AddField(
            model_name='driver',
            name='d_acnum',
            field=models.CharField(max_length=8, default=''),
        ),
        migrations.AddField(
            model_name='driver',
            name='d_phone',
            field=models.CharField(max_length=11, default=''),
        ),
        migrations.AddField(
            model_name='driver',
            name='id',
            field=models.AutoField(primary_key=True, default=1, serialize=False),
        ),
        migrations.AddField(
            model_name='send_driver',
            name='id',
            field=models.AutoField(primary_key=True, default=1, serialize=False),
        ),
        migrations.AddField(
            model_name='send_driver',
            name='sd_acnum',
            field=models.CharField(max_length=8, default=''),
        ),
        migrations.AddField(
            model_name='user',
            name='acnum',
            field=models.CharField(max_length=10, default=''),
        ),
        migrations.AlterField(
            model_name='send_driver',
            name='sd_phone',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, default=1, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.NullBooleanField(default='null'),
        ),
    ]
