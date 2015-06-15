# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdicciones', '0002_auto_20150614_0122'),
    ]

    operations = [
        migrations.AddField(
            model_name='jurisdiccion',
            name='codigo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jurisdiccion',
            name='descripcion',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
