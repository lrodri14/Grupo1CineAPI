from django.urls import path
from .views import FacturarBoletosAPIView, FacturarProductoAPIView

# Define your urls here.

urlpatterns = [
    path('facturar_boleto', FacturarBoletosAPIView.as_view(), name='facturar_boleto'),
    path('facturar_productos', FacturarProductoAPIView.as_view(), name='facturar_productos'),
]