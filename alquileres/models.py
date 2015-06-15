# -*- coding: utf-8 -*-

from django.db import models


class Alquiler (models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    inmueble = models.ForeignKey("Inmueble")
    cuof = models.ForeignKey("jurisdicciones.CUOF")

    def __unicode__(self):
        return "%s - %s" % (self.fecha_inicio, self.fecha_fin)

    class Meta:
        verbose_name_plural = 'Alquileres'


class Inmueble (models.Model):
    domicilio = models.ForeignKey("personas.Domicilio")
    destino = models.TextField()
    mts2 = models.CharField(max_length=100, blank=True, null=True)
    adicional = models.TextField(blank=True, null=True)
    titular = models.ForeignKey("personas.Persona")

    def __unicode__(self):
        return self.destino
