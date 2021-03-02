# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('d_id', models.IntegerField(primary_key=True, max_length=8, serialize=False)),
                ('d_name', models.CharField(max_length=20)),
                ('d_photo', DjangoUeditor.models.UEditorField()),
                ('d_price', models.IntegerField(max_length=4)),
                ('d_exprience', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': '司机',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lev', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name_plural': '用户等级',
            },
        ),
        migrations.CreateModel(
            name='Stars',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('mumber', models.IntegerField(max_length=2)),
            ],
            options={
                'verbose_name_plural': '星级',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=10, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=12)),
                ('sex', models.NullBooleanField(default='')),
                ('identity_id', models.CharField(max_length=18)),
                ('phone', models.IntegerField(max_length=11)),
                ('email', models.CharField(max_length=30)),
                ('level', models.ForeignKey(default='普通', to='RentalWebsite.Level')),
            ],
            options={
                'verbose_name_plural': '用户',
            },
        ),
        migrations.CreateModel(
            name='Vehicle_leasing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('v_type', models.CharField(max_length=30)),
                ('v_price_work', models.IntegerField(max_length=5)),
                ('v_price_week', models.IntegerField(max_length=5)),
                ('v_price_overtime', models.IntegerField(max_length=3)),
                ('v_set', models.IntegerField(max_length=2)),
                ('cash_pledge', models.IntegerField(max_length=6)),
                ('v_addr', models.CharField(max_length=30)),
                ('v_picture', DjangoUeditor.models.UEditorField()),
                ('v_tag', models.ForeignKey(to='RentalWebsite.Tag')),
            ],
            options={
                'verbose_name_plural': '租用车辆',
            },
        ),
        migrations.AddField(
            model_name='driver',
            name='d_star',
            field=models.ForeignKey(to='RentalWebsite.Stars'),
        ),
    ]
