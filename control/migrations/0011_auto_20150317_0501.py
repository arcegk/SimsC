# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0010_auto_20150315_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='meses',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='sim',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
        migrations.AddField(
            model_name='sim',
            name='cliente',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sim',
            name='meses',
            field=models.ManyToManyField(to='control.Mes'),
            preserve_default=True,
        ),
    ]
