from django.db import models
from django.core.validators import EmailValidator
from .validators import validar_celular
from .validators import validar_pais

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class ProductUnits(models.TextChoices):
    units = 'u', 'Unidades',
    kg = 'pc', 'Piezas'

class Product(models.Model):
    nombre = models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    unidades = models.CharField(
        max_length = 2,
        choices = ProductUnits.choices,
        default = ProductUnits.units
    )
    disponible = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"${self.nombre} - ${self.precio}"

class Client(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, validators=[EmailValidator('No es un email valido')])
    celular = models.IntegerField(validators=[validar_celular])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Proveedor(models.Model):
    empresa = models.CharField(max_length=255)
    pais = models.CharField(max_length=20, validators=[validar_pais])
    email = models.EmailField()
    representante = models.CharField(max_length=255)
    celular = models.IntegerField(validators=[validar_celular])

    def __str__(self):
        return self.empresa
