from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .serializers import ClienteAuthSerializer, ClienteSerializer
from utilities.mailing import enviar_correo_bienvenida, enviar_correo_verificacion
from utilities.autenticacion import generar_codigo
from .forms import ClienteForm, ClienteUpdateForm, ClienteCambioContraForm
from .models import Clientes, CodigoVerificacion

User = get_user_model()

# Create your views here.


class AutenticacionAPIView(APIView):
    """
        DOCSTRING: Autenticacion, endpoint responsable de la autenticacion del usuario, manejo de errores y retorno de token
        de autenticacion.
    """
    serializer_class = ClienteAuthSerializer

    def post(self, request):
        # Recoleccion de datos
        email = request.data.get('email')
        contrasena = request.data.get('password')
        # Autenticacion de usuario
        autenticado = authenticate(request, username=email, password=contrasena)
        # Respuesta
        if autenticado is not None:
            token, _ = Token.objects.get_or_create(user=autenticado)
            return Response(data={'data': {'token': token.key}}, status=HTTP_201_CREATED)
        else:
            return Response(data={'error': 'Usuario No Autenticado'}, status=HTTP_401_UNAUTHORIZED)


class CreacionClienteAPIView(APIView):
    """
        DOCSTRING: CreacionCliente, endpoint responsable de la creacion del usuario, manejo de errores y retorno de token
        de autenticacion.
    """
    serializer_class = ClienteSerializer

    def post(self, request):
        # Collect Data
        usuario_form = ClienteForm(data=request.data)
        # Response
        if usuario_form.is_valid():
            usuario = usuario_form.save()
            codigo = CodigoVerificacion.objects.create(codigo=generar_codigo(), cliente=usuario)
            token, _ = Token.objects.get_or_create(user=usuario)
            enviar_correo_bienvenida(usuario.first_name, usuario.last_name, usuario.email)
            enviar_correo_verificacion(usuario.first_name, usuario.last_name, usuario.email, codigo.codigo)
            return Response(data={'data': {'token': token.key}}, status=HTTP_200_OK)
        else:
            return Response(data={'data': {'error': usuario_form.errors}}, status=HTTP_400_BAD_REQUEST)


class ClienteAPIView(APIView):
    """
        DOCSTRING: ClienteAPIView, endpoint responsable del manejo de perfil del cliente
    """
    serializer_class = ClienteSerializer

    def get(self, request, pk=None):
        try:
            cliente = Clientes.objects.get(pk=pk)
            return Response(data={'data': {'cliente': self.serializer_class(cliente).data}}, status=HTTP_200_OK)
        except Clientes.DoesNotExist:
            return Response(data={'error': 'El Cliente no existe'}, status=HTTP_404_NOT_FOUND)

    def patch(self, request, pk=None):
        # Recoleccion de datos
        data = request.data
        try:
            cliente = Clientes.objects.get(pk=pk)
            cliente_form = ClienteUpdateForm(data, instance=cliente)
            if cliente_form.is_valid():
                cliente = cliente_form.save()
                return Response(data={'data': self.serializer_class(cliente).data}, status=HTTP_200_OK)
            else:
                return Response(data={'error': cliente_form.errors}, status=HTTP_400_BAD_REQUEST)
        except:
            return Response(data={'error': 'No se pudo actualizar el usuario'}, status=HTTP_400_BAD_REQUEST)


class ClienteVerificacionAPIView(APIView):
    """
        DOCSTRING: ClienteVerificacionAPIView, endpoint responsable de la verificacion de perfil del cliente
    """

    def post(self, request):
        # Recolectar datos
        try:
            codigo_enviado = request.data.get('codigo')
            codigo = CodigoVerificacion.objects.get(codigo=codigo_enviado)
            usuario = codigo.cliente
            usuario.verificado = True
            usuario.save()
            token, _ = Token.objects.get_or_create(user=usuario)
            return Response(data={'data': {'token': token.key}}, status=HTTP_200_OK)
        except:
            return Response(data={'error': 'Occurio un error al intentar verificar su perfil'}, status=HTTP_400_BAD_REQUEST)


class ClienteSolicitudCambioContrasenaAPIView(APIView):

    """
        DOCSTRING: ClienteCambioContrasenaAPIView, endpoint responsable de generar un codigo de cambio de contraseña
    """

    def post(self, request):
        # Recoleccion de datos

        try:
            email = request.data.get('email')
            cliente = Clientes.objects.get(email=email)
            CodigoVerificacion.objects.create(codigo=generar_codigo(), cliente=cliente)
            return Response(data={'data': {'email': 'Solicitud generada exitosamente'}}, status=HTTP_200_OK)
        except Clientes.DoesNotExist:
            return Response(data={'error': 'Error al generar solicitud de cambio de contraseña'}, status=HTTP_400_BAD_REQUEST)


class ClienteContraVerificacionAPIView(APIView):
    """
        DOCSTRING: ClienteVerificacionAPIView, endpoint responsable de la verificacion de perfil del cliente
    """

    def post(self, request):
        # Recolectar datos
        try:
            codigo_enviado = request.data.get('codigo')
            codigo = CodigoVerificacion.objects.get(codigo=codigo_enviado)
            usuario = codigo.cliente
            token, _ = Token.objects.get_or_create(user=usuario)
            return Response(data={'data': {'email': usuario.email}},
                            status=HTTP_200_OK)
        except:
            return Response(data={'error': 'Occurio un error al intentar verificar su perfil'}, status=HTTP_400_BAD_REQUEST)


class ClienteCambioContraAPIView(APIView):

    """
        DOCSTRING: ClienteCambioContrasenaAPIView, endpoint responsable de generar un codigo de cambio de contraseña
    """

    def post(self, request):
        # Recoleccion de datos
        try:
            email = request.data.get('email')
            cliente = Clientes.objects.get(email=email)
            cliente.set_password(request.data.get('new_password1'))
            cliente.save()
            return Response(data={'data': {'mensaje': 'Contraseña cambiada exitosamente'}}, status=HTTP_200_OK)
        except Clientes.DoesNotExist:
            return Response(data={'error': 'Error al intentar cambio de contraseña'}, status=HTTP_400_BAD_REQUEST)



