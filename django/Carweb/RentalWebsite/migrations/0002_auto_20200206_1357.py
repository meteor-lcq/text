# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send_driver',
            fields=[
                ('sd_id', models.IntegerField(primary_key=True, max_length=8, serialize=False)),
                ('sd_name', models.CharField(max_length=20)),
                ('sd_phone', models.IntegerField(max_length=11)),
                ('sd_photo', DjangoUeditor.models.UEditorField()),
            ],
        ),
        migrations.RenameField(
            model_name='level',
            old_name='lev',
            new_name='lev_zi',
        ),
        migrations.RenameField(
            model_name='vehicle_leasing',
            old_name='cash_pledge',
            new_name='v_cash_pledge',
        ),
        migrations.AddField(
            model_name='level',
            name='lev_num',
            field=models.IntegerField(max_length=1, default=0),
        ),
    ]
