from django.db import models
from django.core.validators import MinValueValidator

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria

class Material(models.Model):

    ESTADOS = [
        ('Disponible', 'Disponible'),
        ('Reservado', 'Reservado'),
        ('Suspendido', 'Suspendido'),
    ]

    nombre = models.CharField(max_length=150)

    descripcion = models.TextField()

    stock = models.PositiveIntegerField(
        validators=[MinValueValidator(0)]
    )

    precio_referencia = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='Disponible'
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT
    )
    
    imagen = models.ImageField(
    upload_to="materiales/",
    blank=True,
    null=True
    )
    
    codigo = models.CharField(
    max_length=20,
    unique=True
    )
    
    activo = models.BooleanField(
        default=True
    )
    
    def __str__(self):
        return self.nombre
