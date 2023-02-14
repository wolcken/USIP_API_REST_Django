from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"category", views.CategoriaViewSet)
router.register(r"product", views.ProductViewSet)
router.register(r"client", views.ClientViewSet)
router.register(r"Provider", views.ProveedorViewSet)

urlpatterns = [
    path("contact/<str:name>", views.contact, name="contact"),
    path("categorias", views.categorias, name="categorias"),
    path("productos", views.productFormView, name="productos"),
    path("clientes", views.clientes, name="clientes"),
    path("proveedores", views.proveedores, name="proveedores"),
    path("custom_products/crear/", views.ProductCreateView.as_view()),
    path("custom_products/cantidad/", views.productos_count),
    path("", include(router.urls)),
]