# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdicciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jurisdiccion',
            options={'verbose_name_plural': 'Jurisdicciones'},
        ),
    ]
