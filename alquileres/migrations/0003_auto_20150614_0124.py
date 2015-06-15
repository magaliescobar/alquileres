# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alquileres', '0002_auto_20150614_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='mts2',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
