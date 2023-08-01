from django.db import models
from django.contrib.auth import get_user_model
from servicios.models import Pelicula
from salas.models import Asiento
from productos.models import Producto

User = get_user_model()

# Create your models here.


class Factura(models.Model):

    id_cliente = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    fecha = models.DateField(blank=False, null=True, auto_now_add=True)
    total = models.FloatField(blank=False, null=False)

    class Meta:
        db_table = 'facturas'


class Pago(models.Model):

    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE, blank=False, null=False)
    metodo_pago = models.CharField(max_length=255, blank=False, null=False)
    monto = models.FloatField(blank=False, null=False)
    fecha_pago = models.DateField(blank=False, null=True, auto_now_add=True)

    class Meta:
        db_table = 'pagos'


class DetalleBoleto(models.Model):

    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE, blank=True, null=True, related_name='factura_detalle')
    id_pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, blank=True, null=True, related_name='pelicula_detalle')
    id_horario = models.ForeignKey(Factura, on_delete=models.CASCADE, blank=True, null=True, related_name='horario_detalle')
    id_asiento = models.ForeignKey(Asiento, on_delete=models.CASCADE, blank=True, null=True, related_name='asiento_detalle')
    precio_unitario = models.FloatField(blank=False, null=False)

    class Meta:
        db_table = 'detallesboleto'


class DetalleProducto(models.Model):

    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE, blank=True, null=True, related_name='factura_producto')
    id_pelicula = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True, related_name='producto_detalle')
    cantidad = models.IntegerField(blank=False, null=False)
    precio_unitario = models.FloatField(blank=False, null=False)

    class Meta:
        db_table = 'detallesproducto'
