# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0006_auto_20150314_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sim',
            name='valor',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
