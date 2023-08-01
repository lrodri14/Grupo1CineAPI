from django.contrib.auth.backends import ModelBackend
from .models import Clientes

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Clientes.objects.get(email=username)
            if user.check_password(password):
                return user
        except Clientes.DoesNotExist:
            return None