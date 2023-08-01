from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, SetPasswordForm

User = get_user_model()

# Define your forms here.

class ClienteForm(UserCreationForm):
    """
        DOCSTRING: ClienteForm, form responsable de la creacion del usuario
    """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',
                  'direccion', 'telefono', 'FechaNac', 'DNI',)


class ClienteUpdateForm(UserChangeForm):

    """
        DOCSTRING: ClienteUpdateForm, form responsable de la actualizacion del usuario
    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'direccion', 'telefono', 'FechaNac', 'DNI', )


class ClienteCambioContraForm(SetPasswordForm):
    """
        DOCSTRING: ClienteCambioContraForm responsable de la actualizacion de contraseña
    """
    pass


