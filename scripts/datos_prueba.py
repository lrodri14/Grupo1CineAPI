import os
import sys
import django
import random
import datetime
from faker import Faker

django_project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinepolis.settings')
sys.path.append(django_project_path)
django.setup()

from ciudades.models import Ciudad
from salas.models import Sala
from servicios.models import Horario, Pelicula

faker = Faker()


def crear_ciudades():
    for ciudad in range(0, 10):
        Ciudad.objects.create(nombre=faker.city())


def crear_salas():
    Ciudades = Ciudad.objects.all()
    for sala in range(0, 50):
        Sala.objects.create(capacidad=random.randint(100, 200), ciudad=random.choice(Ciudades))


def crear_peliculas():
    for i in range(0, 100):
        Pelicula.objects.create(titulo=faker.sentence(nb_words=5), duracion=random.randint(80, 200), genero=random.choice(['Horror', 'Accion', 'Suspenso']),
                                sinopsis=faker.paragraph(nb_sentences=3), actores='Tom Cruise', estado=random.randint(1, 4), clasificacion=random.choice(['G', 'PG', 'PG-13']))


def crear_horarios():
    salas = Sala.objects.all()
    peliculas = Pelicula.objects.all()
    start_time = datetime.datetime(2023, 7, 27, random.randint(9, 20), random.randint(0, 59))
    end_time = start_time + datetime.timedelta(hours=random.randint(1, 3), minutes=random.randint(0, 59))

    for i in range(0, 20):
        Horario.objects.create(hora_inicio=start_time.time(), hora_fin=end_time.time(), id_sala=random.choice(salas), id_pelicula=random.choice(peliculas))
    print(Horario.objects.all())


if __name__ == '__main__':
    crear_horarios()
