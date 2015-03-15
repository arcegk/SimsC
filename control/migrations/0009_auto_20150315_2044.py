# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0008_auto_20150314_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='sim',
            field=models.ForeignKey(to='control.Sim', unique=True),
            preserve_default=True,
        ),
    ]
