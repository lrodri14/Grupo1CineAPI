from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from servicios.serializers import PeliculaSerializer, HorarioSerializer
from ciudades.models import Ciudad
from servicios.models import Pelicula, Horario

# Create your views here.


class PeliculasAPIView(APIView):

    serializer_class = PeliculaSerializer

    def get(self, request):
        # Recolectar datos
        estado = request.GET.get('estado')
        try:
            peliculas = Pelicula.objects.filter(estado=estado)
            return Response(data={'data': {'peliculas': self.serializer_class(peliculas, many=True).data}}, status=HTTP_200_OK)
        except:
            return Response(data={'error': 'Error al extraer las peliculas en cine'}, status=HTTP_400_BAD_REQUEST)


class PeliculaAPIView(APIView):

    serializer_class = PeliculaSerializer

    def get(self, request, pk):
        # Recoleccion de datos
        id_ciudad = request.GET.get('ciudad')
        try:
            ciudad = Ciudad.objects.get(pk=id_ciudad)
            pelicula = Pelicula.objects.get(pk=pk)
            horarios = Horario.objects.filter(id_sala__ciudad=ciudad, id_pelicula=pelicula)
            return Response(data={'data': {'pelicula': PeliculaSerializer(pelicula).data},
                                           'horarios': HorarioSerializer(horarios, many=True).data}, status=HTTP_200_OK)
        except Ciudad.DoesNotExist:
            return Response(data={'error': 'No se ha encontrado esa pelicula'}, status=HTTP_400_BAD_REQUEST)
