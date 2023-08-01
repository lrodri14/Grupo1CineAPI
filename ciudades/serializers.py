from rest_framework import serializers
from .models import Ciudad

# Define your serializers here.


class CiudadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ciudad
        fields = '__all__'