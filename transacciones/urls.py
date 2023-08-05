from django.urls import path
from .views import FacturarBoletosAPIView

# Define your urls here.

urlpatterns = [
    path('facturar_boleto', FacturarBoletosAPIView.as_view(), name='facturar_boleto'),
]