# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0030_auto_20200330_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('content', models.CharField(max_length=1000)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('browse', models.IntegerField(max_length=50, default=0)),
            ],
            options={
                'verbose_name_plural': '新闻',
            },
        ),
        migrations.CreateModel(
            name='Tag_news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tag', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': '新闻标签',
            },
        ),
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.ForeignKey(to='RentalWebsite.Tag_news'),
        ),
    ]
