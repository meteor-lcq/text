# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0015_auto_20200218_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Func',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': '车用',
            },
        ),
        migrations.AddField(
            model_name='vehicle_leasing',
            name='v_func',
            field=models.ForeignKey(null=True, to='RentalWebsite.Func'),
        ),
    ]
