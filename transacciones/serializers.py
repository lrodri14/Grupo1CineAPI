from rest_framework import serializers
from .models import DetalleBoleto, Factura

# Define your serializers here.


class FacturaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factura
        fields = '__all__'


class DetalleBoletoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleBoleto
        fields = '__all__'


