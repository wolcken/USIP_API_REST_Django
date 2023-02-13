from django.shortcuts import render
from django.http import HttpResponse
from .models import Categoria
# Create your views here.

def index(request):
    return HttpResponse("Hola Mundo")

def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de Django")

def categorias(request):
    categorias = Categoria.objects.all()
    #filt_nomb = request.GET.get("nombre")
    #nombre = Categoria.objects.filter(nombre__contains = filt_nomb)
    return render(request, "categorias.html", {
        #"categorias": nombre
        "categorias": categorias
    })
