# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CUOF',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('oficina', models.IntegerField()),
                ('anexo', models.IntegerField()),
                ('denominacion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jurisdiccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('area', models.CharField(max_length=100)),
                ('subarea', models.CharField(max_length=100)),
                ('oficina', models.CharField(max_length=100)),
                ('dependencia', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='cuof',
            name='jurisdiccion',
            field=models.ForeignKey(to='jurisdicciones.Jurisdiccion'),
        ),
        migrations.AddField(
            model_name='cuof',
            name='responsable',
            field=models.ForeignKey(to='personas.Persona'),
        ),
    ]
