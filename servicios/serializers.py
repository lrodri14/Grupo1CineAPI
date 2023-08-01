from rest_framework import serializers
from salas.serializers import SalaSerializer
from .models import Pelicula, Horario

# Define your serializers here.


class PeliculaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pelicula
        fields = '__all__'


class PeliculaSubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pelicula
        fields = ('id', 'imagen', 'titulo', 'estado', )


class HorarioSerializer(serializers.ModelSerializer):

    sala = SalaSerializer(source='id_sala')
    pelicula = PeliculaSubSerializer(source='id_pelicula')

    class Meta:
        model = Horario
        fields = ('sala', 'pelicula', 'hora_inicio', )