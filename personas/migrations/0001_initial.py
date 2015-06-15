# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calle', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('barrio', models.CharField(max_length=100, null=True, blank=True)),
                ('adicional', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=100, choices=[(b'fisica', b'F\xc3\xadsica'), (b'juridica', b'Jur\xc3\xaddica')])),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100, null=True, blank=True)),
                ('cuit_cuil', models.CharField(max_length=15)),
                ('dni', models.IntegerField(null=True, blank=True)),
                ('telefono', models.CharField(max_length=40, null=True, blank=True)),
                ('domicilio', models.ForeignKey(blank=True, to='personas.Domicilio', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='localidad',
            name='provincia',
            field=models.ForeignKey(to='personas.Provincia'),
        ),
        migrations.AddField(
            model_name='domicilio',
            name='localidad',
            field=models.ForeignKey(to='personas.Localidad'),
        ),
    ]
