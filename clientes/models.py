from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):

    """
        DOCSTRING: CustomUserManager responsable de la creacion de usuarios a nivel de cliente y adminitracion.
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El email es un campo requerido")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe de contener la propiedad is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe de contener la propiedad is_superuser=True')

        return self.create_user(email, password, **extra_fields)


class Clientes(AbstractUser):
    """
        DOCSTRING: Clase responsable de la autentication del usuario
    """
    first_name = models.CharField(max_length=255, blank=True, null=True, default=None)
    last_name = models.CharField(max_length=255, blank=True, null=True, default=None)
    email = models.EmailField(unique=True, blank=True, null=True, default=None)
    direccion = models.CharField(max_length=255, blank=True, null=True, default=None)
    telefono = models.CharField(max_length=255, blank=True, null=True, default=None)
    FechaNac = models.DateField(blank=True, null=True, default=None)
    DNI = models.CharField(max_length=255, blank=True, null=True, default=None)
    verificado = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        db_table = 'clientes'

    def save(self, *args, **kwargs):
        self.username = self.DNI if self.DNI else 'admin'
        super().save(*args, **kwargs)

    def __str__(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return 'Administrator'


class CodigoVerificacion(models.Model):
    """
       DOCSTRING: Clase responsable del manejo de codigos de verificacion de usuarios registrados
    """
    codigo = models.CharField(max_length=6, blank=False, null=False, default=None)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.codigo
