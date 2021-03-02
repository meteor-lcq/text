# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import DjangoUeditor.models


class Migration(migrations.Migration):

    dependencies = [
        ('RentalWebsite', '0031_auto_20200401_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=DjangoUeditor.models.UEditorField(),
        ),
    ]
