# Generated by Django 4.2.3 on 2023-07-27 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('salas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, unique=True)),
                ('duracion', models.CharField(max_length=255)),
                ('genero', models.CharField(max_length=255)),
                ('sinopsis', models.TextField()),
                ('imagen', models.ImageField(upload_to='banners/')),
                ('actores', models.TextField()),
                ('estado', models.BooleanField(default=True)),
                ('clasificacion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('id_pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.pelicula')),
                ('id_sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salas.sala')),
            ],
        ),
    ]
