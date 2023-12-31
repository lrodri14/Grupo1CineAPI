from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.authentication import TokenAuthentication
from servicios.models import Pelicula, Horario
from salas.models import Asiento
from productos.models import Producto
from transacciones.models import Factura, DetalleBoleto, DetalleProducto
from .serializers import DetalleBoletoSerializer, FacturaSerializer
from productos.serializers import ProductoSerializer
from utilities.mailing import enviar_correo_boletos, enviar_correo_productos

# Create your views here.

class FacturasAPIView(APIView):
    """
        DOCSTRING: FacturasAPIVew, responsable de la extraccion de facturas
    """
    authentication_classes = [TokenAuthentication]
    serializer_class = FacturaSerializer

    def get(self, request):
        try:
            # Recoleccion de datos
            cliente = request.user
            facturas = Factura.objects.filter(id_cliente=cliente)
            return Response(data={'data': {'facturas': self.serializer_class(facturas, many=True)}}, status=HTTP_200_OK)
        except Factura.DoesNotExist:
            return Response(data={'error': 'No se pueden extraer las facturas'}, status=HTTP_500_INTERNAL_SERVER_ERROR)



class FacturarBoletosAPIView(APIView):
    """
        DOCSTRING: FacturarBoletosAPIView, responsable de la facturacion de asientos
    """

    authentication_classes = [TokenAuthentication]
    serializer_class = DetalleBoletoSerializer

    def post(self, request):
        try:
            # Recoleccion de datos
            user = request.user
            id_asientos = request.data.get('asientos')
            id_horario = request.data.get('id_horario')
            id_sala = request.data.get('id_sala')
            total = request.data.get('total')
            # Extraccion de datos
            horario = Horario.objects.get(pk=id_horario)
            pelicula = horario.id_pelicula
            factura = Factura.objects.create(id_cliente=user, total=total)
            for asiento_id in id_asientos:
                asiento = Asiento.objects.get(fila=asiento_id[1], numero=asiento_id[0], id_sala=id_sala)
                DetalleBoleto.objects.create(id_factura=factura,
                                             id_pelicula=pelicula,
                                             id_horario=horario,
                                             id_asiento=asiento,
                                             precio_unitario=pelicula.precio)
                asiento.ocupado = True
                asiento.save()
            boletos = DetalleBoleto.objects.all()
            enviar_correo_boletos(user.first_name, user.last_name, user.email, factura.id)
            return Response(data={'data': {'detalles': self.serializer_class(boletos, many=True).data}})
        except Pelicula.DoesNotExist as e:
            return Response(data={'error': 'Error al create detalle de boleto'}, status=HTTP_404_NOT_FOUND)
        except Horario.DoesNotExist:
            return Response(data={'error': 'Error al create detalle de boleto'}, status=HTTP_404_NOT_FOUND)
        except:
            return Response(data={'error': 'Error al create detalle de boleto'}, status=HTTP_500_INTERNAL_SERVER_ERROR)


class FacturarProductoAPIView(APIView):
    """
        DOCSTRING: APIView responsable de la facturacion de productos
    """
    authentication_classes = [TokenAuthentication]
    serializer_class = ProductoSerializer

    def post(self, request):
        try:
            # Recoleccion de datos
            cliente = request.user
            productos = request.data.get('golosinas')
            total = request.data.get('total')
            # Creacion de factura
            factura = Factura.objects.create(id_cliente=cliente, total=total)
            for producto in productos:
                producto_seleccionado = Producto.objects.get(pk=producto[0])
                DetalleProducto.objects.create(id_factura=factura,
                                               id_producto=producto_seleccionado,
                                               cantidad=producto[1],
                                               precio_unitario=producto_seleccionado.precio)
            enviar_correo_productos(cliente.first_name, cliente.last_name, factura.id, cliente.email)
            return Response(data={'data': 'Productos facturados correctamente'}, status=HTTP_200_OK)
        except:
            return Response(data={'error': 'Error en la facturacion de productos'}, status=HTTP_500_INTERNAL_SERVER_ERROR)

