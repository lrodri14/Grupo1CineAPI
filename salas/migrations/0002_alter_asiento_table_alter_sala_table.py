# Generated by Django 4.2.3 on 2023-07-27 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='asiento',
            table='asientos',
        ),
        migrations.AlterModelTable(
            name='sala',
            table='salas',
        ),
    ]
