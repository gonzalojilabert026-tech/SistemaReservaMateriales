from django.db import models


class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria


class Material(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    stock = models.IntegerField()
    precio_referencia = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nombre