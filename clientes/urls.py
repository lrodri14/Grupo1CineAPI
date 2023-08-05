from django.urls import path
from .views import AutenticacionAPIView, CreacionClienteAPIView, ClienteAPIView, ClienteVerificacionAPIView,\
    ClienteSolicitudCambioContrasenaAPIView, ClienteContraVerificacionAPIView, ClienteCambioContraAPIView

# Define your urls here.

urlpatterns = [
    path('', AutenticacionAPIView.as_view(), name='auth'),
    path('registro', CreacionClienteAPIView.as_view(), name='registro'),
    path('verificacion', ClienteVerificacionAPIView.as_view(), name='verificacion'),
    path('solicitud_cambio_contra', ClienteSolicitudCambioContrasenaAPIView.as_view(), name='solicitud_cambio_contra'),
    path('verificacion_contra', ClienteContraVerificacionAPIView.as_view(), name='verificacion_contra'),
    path('cambio_contra', ClienteCambioContraAPIView.as_view(), name='cambio_contra'),
    path('cliente', ClienteAPIView.as_view(), name='cliente_perfil'),
]