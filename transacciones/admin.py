from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Factura)
admin.site.register(Pago)
admin.site.register(DetalleBoleto)
admin.site.register(DetalleProducto)

