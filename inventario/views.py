from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Categoria
from .models import Product
from .models import Client
from .models import Proveedor
from .forms import ProductForm
from .forms import ClientForm
from .forms import ProveedorForm

from rest_framework import viewsets
from rest_framework import generics
from .serializers import CategoriaSerializer
from .serializers import ProductSerializer
from .serializers import ClientSerializer
from .serializers import ProveedorSerializer

from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de Django")

def categorias(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre:
        q = Categoria(nombre = post_nombre)
        q.save()

    filtro_nombre = request.GET.get('nombre')
    if filtro_nombre:
        categorias = Categoria.objects.filter(nombre__contains = filtro_nombre)
    else:
        categorias = Categoria.objects.all

    return render(request, "form_categorias.html", {
        "categorias": categorias
    })

def productFormView(request):
    form = ProductForm()
    product = None
    id_product = request.GET.get('id')
    if id_product:
        product = get_object_or_404(Product, id=id_product)
        form = ProductForm(instance=product)

    if request.method == 'POST':
        if product:
            form = ProductForm(request.POST, instance=product)
        else:
            form = ProductForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "form_products.html", {"form": form})

def clientes(request):
    form = ClientForm()
    client = None
    id_client = request.GET.get('id')
    if id_client:
        client = get_object_or_404(Client, id=id_client)
        form = ClientForm(instance=client)

    if request.method == 'POST':
        if client:
            form = ClientForm(request.POST, instance=client)
        else:
            form = ClientForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "form_clients.html", {"form": form})

def proveedores(request):
    form = ProveedorForm()
    proveedor = None
    id_proveedor = request.GET.get('id')
    if id_proveedor:
        proveedor = get_object_or_404(Proveedor, id=id_proveedor)
        form = ProveedorForm(instance=proveedor)

    if request.method == 'POST':
        if proveedor:
            form = ProveedorForm(request.POST, instance=proveedor)
        else:
            form = ProveedorForm(request.POST)

    if form.is_valid():
        form.save()

    return render(request, "form_proveedores.html", {"form": form})


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

"""Custom API"""
class ProductCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(["GET"])
def productos_count(request):
    try:
        cantidad = Product.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
            safe=False,
            status=200,
        )
    except Exception as e:
        return JsonResponse({"message": str(e)},status=400)