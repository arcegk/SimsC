# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0009_auto_20150315_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sim',
            name='valor',
            field=models.DecimalField(default=0, max_digits=200, decimal_places=1, blank=True),
            preserve_default=True,
        ),
    ]
