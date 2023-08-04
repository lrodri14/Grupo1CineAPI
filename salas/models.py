from django.db import models
from ciudades.models import Ciudad

# Create your models here.

class Sala(models.Model):
    """
        DOCSTRING: Modelo Sala, responsable de la creacion de salas del cine.
    """

    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, blank=False, null=False, related_name='ciudad_sala')
    capacidad = models.IntegerField(blank=False, null=False)

    class Meta:
        db_table = 'salas'
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'

    def __str__(self):
        return 'Sala #{} en {}'.format(self.id, self.ciudad.nombre)


class Asiento(models.Model):
    """
        DOCSTRING: Modelo Asiento, responsable de la creacion de asientos de sala del cine.
    """
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE, blank=False, null=False, related_name='sala_asientos')
    fila = models.CharField(max_length=255, blank=False, null=False)
    numero = models.IntegerField(blank=False, null=False)
    ocupado = models.BooleanField(blank=False, null=False, default=False)

    class Meta:
        db_table = 'asientos'
        verbose_name = 'Asiento'
        verbose_name_plural = 'Asientos'

    def __str__(self):
        return 'Asiento {}{} - {}'.format(self.numero, self.fila, self.id_sala.ciudad.nombre)


