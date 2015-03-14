# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0005_auto_20150314_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sim',
            name='numero',
            field=models.CharField(max_length=15, unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
