# Generated by Django 4.2.3 on 2023-08-04 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0006_remove_horario_hora_fin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='horario',
            options={'verbose_name': 'Horario', 'verbose_name_plural': 'Horarios'},
        ),
        migrations.AlterModelOptions(
            name='pelicula',
            options={'verbose_name': 'Pelicula', 'verbose_name_plural': 'Peliculas'},
        ),
    ]
