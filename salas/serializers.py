from rest_framework import serializers
from ciudades.serializers import CiudadSerializer
from .models import Sala, Asiento

# Define your serializers here.


class SalaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sala
        fields = ('id', )


class AsientoSerializer(serializers.ModelSerializer):

    id_sala = SalaSerializer()

    class Meta:
        model = Asiento
        fields = '__all__'
