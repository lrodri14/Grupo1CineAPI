from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import CiudadSerializer
from .models import Ciudad

# Create your views here.


class CiudadAPIView(APIView):
    """
        DOCSTRING: CiudadAPIView, responsable de la extraccion de ciudades
    """
    serializer_class = CiudadSerializer

    def get(self, request):
        try:
            ciudades = Ciudad.objects.all()
            return Response(data={'data': {'ciudades': self.serializer_class(ciudades, many=True).data}}, status=HTTP_200_OK)
        except:
            return Response(data={'error': {'mensaje': 'Ocurrio un error al extraer ciudades'}}, status=HTTP_400_BAD_REQUEST)
