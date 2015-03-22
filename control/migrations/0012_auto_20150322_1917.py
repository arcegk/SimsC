# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0011_auto_20150317_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sim',
            name='cliente',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sim',
            name='meses',
            field=models.ManyToManyField(to='control.Mes', null=True),
            preserve_default=True,
        ),
    ]
