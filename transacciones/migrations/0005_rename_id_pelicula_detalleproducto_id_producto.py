# Generated by Django 4.2.3 on 2023-08-06 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transacciones', '0004_alter_detalleboleto_precio_unitario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalleproducto',
            old_name='id_pelicula',
            new_name='id_producto',
        ),
    ]