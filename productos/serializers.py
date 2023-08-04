from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    """
        DOCSTRING: ProductoSerializer, responsable de la serializacion de datos de productos
    """
    class Meta:
        model = Producto
        fields = '__all__'