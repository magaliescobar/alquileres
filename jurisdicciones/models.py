from django.db import models


class CUOF (models.Model):
    oficina = models.IntegerField()
    anexo = models.IntegerField()
    denominacion = models.CharField(max_length=100)
    responsable = models.ForeignKey("personas.Persona")
    jurisdiccion = models.ForeignKey("Jurisdiccion")

    def __unicode__(self):
        return "%s - %s - %s - %s" % (
            self.oficina, self.anexo, self.denominacion,
            self.responsable
        )


class Jurisdiccion (models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    subarea = models.CharField(max_length=100)
    oficina = models.CharField(max_length=100)
    dependencia = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s - %s " % (self.codigo, self.descripcion)

    class Meta:
        verbose_name_plural = 'Jurisdicciones'
