from django import forms
from .models import Product
from .models import Client
from .models import Proveedor

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = "__all__"