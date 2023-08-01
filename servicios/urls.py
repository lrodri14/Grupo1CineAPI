from django.urls import path
from .views import PeliculasAPIView, PeliculaAPIView

# Define your urls here.

urlpatterns = [
    path('', PeliculasAPIView.as_view(), name='peliculas'),
    path('<int:pk>', PeliculaAPIView.as_view(), name='pelicula')
]