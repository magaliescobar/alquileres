# -*- coding: utf-8 -*-

from django.db import models


class Persona (models.Model):
    FISICA = "fisica"
    JURIDICA = "juridica"
    TIPOS = (
        (FISICA, "Física"),
        (JURIDICA, "Jurídica"),
    )

    tipo = models.CharField(max_length=100, choices=TIPOS)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    cuit_cuil = models.CharField(max_length=15)
    dni = models.IntegerField(blank=True, null=True)
    domicilio = models.ForeignKey("Domicilio", blank=True, null=True)
    telefono = models.CharField(max_length=40, blank=True, null=True)

    def __unicode__(self):
        if not self.apellidos:
            return "%s, %s" % (self.nombre,
                               self.cuit_cuil)
        return "%s, %s, %s" % (self.apellidos, self.nombre, self.cuit_cuil)


class Domicilio (models.Model):
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()
    barrio = models.CharField(max_length=100, blank=True, null=True)
    adicional = models.TextField(blank=True, null=True)
    localidad = models.ForeignKey("Localidad")

    def __unicode__(self):
        return "%s, %s" % (self.calle, self.numero)


class Localidad (models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey("Provincia")

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Localidades'


class Provincia (models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre
