from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class ProductUnits(models.TextChoices):
    units = 'u', 'Unidades',
    kg = 'kg', 'Kilogramos'

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