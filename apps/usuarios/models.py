from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):

    ROLES = [
        ("ADMIN", "Administrador"),
        ("CLIENTE", "Cliente")
    ]

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    rut = models.CharField(
        max_length=12
    )

    telefono = models.CharField(
        max_length=20
    )

    rol = models.CharField(
        max_length=20,
        choices=ROLES,
        default="CLIENTE"
    )

    def __str__(self):

        return self.usuario.username