# Generated by Django 4.2.3 on 2023-07-29 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_alter_clientes_direccion_alter_clientes_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='first_name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='last_name',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
