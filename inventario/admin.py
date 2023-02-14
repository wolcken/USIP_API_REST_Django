from django.contrib import admin
from .models import Categoria
from .models import Product
from .models import Client
from .models import Proveedor

# Register your models here.

"""Categoria"""
admin.site.register(Categoria)

"""Product"""
class ProductAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "unidades", "disponible",)
    ordering = ["precio"]
    search_fields = ["nombre"]
    list_filter = ("disponible",)

admin.site.register(Product, ProductAdmin)

"""Client"""
class ClientAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "celular")
    ordering = ["apellido"]
    search_fields = ["apellido"]

admin.site.register(Client, ClientAdmin)

"""Proveedor"""
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("empresa", "pais", "email", "representante", "celular")
    ordering = ["empresa"]
    search_fields = ["representante"]

admin.site.register(Proveedor, ProveedorAdmin)