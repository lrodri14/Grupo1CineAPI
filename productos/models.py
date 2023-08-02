from django.db import models

# Create your models here.

class Producto(models.Model):
    """
        DOCSTRING: Modelo responsable de la creacion de productos
    """
    nombre = models.CharField(max_length=255, blank=False, null=True)
    precio = models.FloatField(blank=False, null=False)
    descripcion = models.TextField(blank=False, null=True)
    imagen = models.ImageField(blank=False, null=False)

    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre