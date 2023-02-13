from django.contrib import admin
from .models import Categoria
from .models import Product

# Register your models here.

admin.site.register(Categoria)
#admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "unidades", "disponible",)
    ordering = ["precio"]
    search_fields = ["nombre"]
    list_filter = ("disponible",)

admin.site.register(Product, ProductAdmin)