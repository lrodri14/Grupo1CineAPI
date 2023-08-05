from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.authentication import TokenAuthentication
from servicios.models import Pelicula, Horario
from salas.models import Asiento
from transacciones.models import Factura, DetalleBoleto
from .serializers import DetalleBoletoSerializer

# Create your views here.


class FacturarBoletosAPIView(APIView):
    """
        DOCSTRING: FacturarBoletosAPIView, responsable de la facturacion de asientos
    """

    authentication_classes = [TokenAuthentication]
    serializer_class = DetalleBoletoSerializer

    def post(self, request):
        # try:
            # Recoleccion de datos
            user = request.user
            id_asientos = request.data.get('asientos')
            id_horario = request.data.get('id_horario')
            total = request.data.get('total')
            # Extraccion de datos
            horario = Horario.objects.get(pk=id_horario)
            pelicula = horario.id_pelicula
            factura = Factura.objects.create(id_cliente=user, total=total)
            for asiento_id in id_asientos:
                asiento = Asiento.objects.get(fila=asiento_id[1], numero=asiento_id[0])
                DetalleBoleto.objects.create(id_factura=factura,
                                             id_pelicula=pelicula,
                                             id_horario=horario,
                                             id_asiento=asiento,
                                             precio_unitario=pelicula.precio)
            boletos = DetalleBoleto.objects.all()
            return Response(data={'data': {'detalles': self.serializer_class(boletos, many=True).data}})
        # except Pelicula.DoesNotExist as e:
        #     return Response(data={'error': 'Error al create detalle de boleto'}, status=HTTP_404_NOT_FOUND)
        # except Horario.DoesNotExist:
        #     return Response(data={'error': 'Error al create detalle de boleto'}, status=HTTP_404_NOT_FOUND)
        # except:
        #     return Response(data={'error': 'Error al create detalle de boleto'}, status=HTTP_500_INTERNAL_SERVER_ERROR)
        #
        #
