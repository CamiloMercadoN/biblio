from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

from .models import Libro, Categoria
from .serializers import LibroSerializador, CategoriaSerializador

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializador


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all().order_by("id")
    serializer_class = LibroSerializador

    @action(detail=True, methods=['post'])
    def prestar(self, request, pk=None):
        libro = self.get_object()
        if not libro.disponible:
            return Response({"detail": "El libro ya está prestado."}, status=status.HTTP_400_BAD_REQUEST)

        usuario = request.data.get("user")
        if not usuario:
            return Response({"detail": "Se requiere el campo 'user'."}, status=status.HTTP_400_BAD_REQUEST)

        libro.disponible = False
        libro.prestado_a = usuario
        libro.fecha_prestamo = timezone.now()
        libro.save()
        return Response(self.get_serializer(libro).data)

    @action(detail=True, methods=['post'])
    def devolver(self, request, pk=None):
        libro = self.get_object()
        if libro.disponible:
            return Response({"detail": "El libro no está prestado."}, status=status.HTTP_400_BAD_REQUEST)

        libro.disponible = True
        libro.prestado_a = None
        libro.fecha_prestamo = None
        libro.save()
        return Response(self.get_serializer(libro).data)