from django.db import models

# Create your models here.

class Ciudad(models.Model):
    """
        DOCSTRING: Modelo ciudad, responsable de la creacion de ubicaciones del cine.
    """
    nombre = models.CharField(max_length=255, blank=False, null=False, unique=True)

    class Meta:
        db_table = 'ciudades'
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return self.nombre