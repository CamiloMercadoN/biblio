from django.urls import path
from .views import (
    EstadoAPIView,
    LibroDetalleAPIView,
    LibroListaCrearAPIView,
    PrestamoLibroAPIView,
    DevolucionLibroAPIView,
)

urlpatterns = [
    path("", EstadoAPIView.as_view(), name="api-salud"),
    path("libros/", LibroListaCrearAPIView.as_view(), name="api-libro-lista"),
    path("libros/<int:pk>/", LibroDetalleAPIView.as_view(), name="api-libro-detalle"),
    path("libros/<int:pk>/prestar/", PrestamoLibroAPIView.as_view(), name="api-libro-prestar"),
    path("libros/<int:pk>/devolver/", DevolucionLibroAPIView.as_view(), name="api-libro-devolver"),
]
