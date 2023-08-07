from django.urls import path
from .views import FacturarBoletosAPIView, FacturarProductoAPIView, FacturasAPIView

# Define your urls here.

urlpatterns = [
    path('facturas', FacturasAPIView.as_view(), name='facturas'),
    path('facturar_boleto', FacturarBoletosAPIView.as_view(), name='facturar_boleto'),
    path('facturar_productos', FacturarProductoAPIView.as_view(), name='facturar_productos'),
]