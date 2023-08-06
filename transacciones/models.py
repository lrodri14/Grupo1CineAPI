from django.db import models
from django.contrib.auth import get_user_model
from servicios.models import Pelicula, Horario
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
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __str__(self):
        return "Factura de {} {}".format(self.id_cliente.first_name, self.id_cliente.last_name)


class Pago(models.Model):

    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE, blank=False, null=False)
    metodo_pago = models.CharField(max_length=255, blank=False, null=False)
    monto = models.FloatField(blank=False, null=False)
    fecha_pago = models.DateField(blank=False, null=True, auto_now_add=True)

    class Meta:
        db_table = 'pagos'
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'


class DetalleBoleto(models.Model):
    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE, blank=True, null=True, related_name='factura_detalle')
    id_pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, blank=True, null=True, related_name='pelicula_detalle')
    id_horario = models.ForeignKey(Horario, on_delete=models.CASCADE, blank=True, null=True, related_name='horario_detalle')
    id_asiento = models.ForeignKey(Asiento, on_delete=models.CASCADE, blank=True, null=True, related_name='asiento_detalle')
    precio_unitario = models.FloatField(blank=True, null=True, default=0.00)

    class Meta:
        db_table = 'detallesboleto'
        verbose_name = 'Detalle de Boleto'
        verbose_name_plural = 'Detalles de Boletos'

    def __str__(self):
        return "Detalle de Boleto: {}".format(self.id_pelicula.titulo)


class DetalleProducto(models.Model):

    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE, blank=True, null=True, related_name='factura_producto')
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True, related_name='producto_detalle')
    cantidad = models.IntegerField(blank=False, null=False)
    precio_unitario = models.FloatField(blank=False, null=False)

    class Meta:
        db_table = 'detallesproducto'
        verbose_name = 'Detalle de Producto'
        verbose_name_plural = 'Detalles de Productos'

    def __str__(self):
        return "Detalle de Producto: {}".format(self.id_producto.nombre)

