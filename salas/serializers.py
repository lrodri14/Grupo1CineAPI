from rest_framework import serializers
from ciudades.serializers import CiudadSerializer
from .models import Sala

# Define your serializers here.


class SalaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sala
        fields = ('id', )
