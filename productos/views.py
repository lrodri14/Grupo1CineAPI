from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_500_INTERNAL_SERVER_ERROR
from .serializers import ProductoSerializer
from .models import Producto
# Create your views here.


class ProductoAPIView(APIView):
    """
        DOCSTRING: ProductoAPIView, responsable de la extraccion de Productos
    """
    serializer_class = ProductoSerializer

    def get(self, request):
        try:
            productos = Producto.objects.all()
            return Response(data={'data': {'productos': self.serializer_class(productos, many=True).data}}, status=HTTP_200_OK)
        except:
            return Response(data={'error': 'Error al extraer los productos'}, status=HTTP_500_INTERNAL_SERVER_ERROR)


