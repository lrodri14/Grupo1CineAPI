from django.db import models
from salas.models import Sala

# Create your models here.


class Pelicula(models.Model):
    """
        DOCSTRING: Modelo responsable de la creacion de peliculas como servicio
    """
    titulo = models.CharField(max_length=255, blank=False, null=False, unique=True)
    duracion = models.CharField(max_length=255, blank=False, null=False)
    genero = models.CharField(max_length=255, blank=False, null=False)
    sinopsis = models.TextField(blank=False, null=False)
    imagen = models.ImageField(blank=True, null=True, upload_to='banners/')
    actores = models.TextField(blank=False, null=False)
    estado = models.IntegerField(blank=False, null=False, default=True)
    clasificacion = models.TextField(blank=False, null=False)

    class Meta:
        db_table = 'peliculas'

    def __str__(self):
        return self.titulo


class Horario(models.Model):
    """
        DOCSTRING: Modelo responsable de la creacion de horarios como servicio
    """
    hora_inicio = models.TimeField(blank=False, null=False)
    id_sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='sala_horario')
    id_pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name='pelicula_horario')

    class Meta:
        db_table = 'horarios'

    def __str__(self):
        return str(self.hora_inicio)


