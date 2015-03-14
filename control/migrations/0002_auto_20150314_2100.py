# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sim',
            name='numero',
            field=models.CharField(max_length=15, blank=True),
            preserve_default=True,
        ),
    ]
