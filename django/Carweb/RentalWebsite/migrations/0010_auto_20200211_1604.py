# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0009_auto_20200211_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sex', models.CharField(max_length=6, default='保密')),
            ],
            options={
                'verbose_name_plural': '性别',
            },
        ),
        migrations.AlterField(
            model_name='state',
            name='id',
            field=models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.ForeignKey(to='RentalWebsite.Sex'),
        ),
    ]
