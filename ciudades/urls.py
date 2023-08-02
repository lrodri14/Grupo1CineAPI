from django.urls import path
from .views import CiudadAPIView

# Define your urls here.

urlpatterns = [
    path('', CiudadAPIView.as_view(), name='ciudad')
]