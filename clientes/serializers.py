from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# Define your serializers here.


class ClienteAuthSerializer(serializers.Serializer):
    """
        DOCSTRING: UserAuthSerializer, responsable de la serializacion de credenciales de usuario.
    """
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class ClienteSerializer(serializers.ModelSerializer):
    """
        DOCSTRING: ClienteSerializer, responsable de la serializacion de informacion de Usuario.
    """

    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',
                  'direccion', 'telefono', 'FechaNac', 'DNI',)
