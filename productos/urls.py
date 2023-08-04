from django.urls import path
from .views import ProductoAPIView

# Define your urls here.

urlpatterns = [
    path('', ProductoAPIView.as_view(), name='productos')
]