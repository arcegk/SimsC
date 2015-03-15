# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0007_auto_20150314_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='sim',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2015, 3, 14, 23, 54, 12, 102603, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='meses',
            field=models.ManyToManyField(to='control.Mes'),
            preserve_default=True,
        ),
    ]
