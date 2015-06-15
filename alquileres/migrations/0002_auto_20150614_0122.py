# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alquileres', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alquiler',
            options={'verbose_name_plural': 'Alquileres'},
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='destino',
            field=models.TextField(),
        ),
    ]
