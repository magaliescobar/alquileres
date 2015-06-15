# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jurisdicciones', '0001_initial'),
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('cuof', models.ForeignKey(to='jurisdicciones.CUOF')),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mts2', models.CharField(max_length=100)),
                ('destino', models.TextField(null=True, blank=True)),
                ('adicional', models.TextField(null=True, blank=True)),
                ('domicilio', models.ForeignKey(to='personas.Domicilio')),
                ('titular', models.ForeignKey(to='personas.Persona')),
            ],
        ),
        migrations.AddField(
            model_name='alquiler',
            name='inmueble',
            field=models.ForeignKey(to='alquileres.Inmueble'),
        ),
    ]
