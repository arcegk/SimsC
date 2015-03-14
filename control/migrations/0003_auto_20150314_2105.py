# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_auto_20150314_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sim',
            name='ide',
            field=models.CharField(unique=True, max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sim',
            name='numero',
            field=models.CharField(unique=True, max_length=15, blank=True),
            preserve_default=True,
        ),
    ]
