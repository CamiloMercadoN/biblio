from rest_framework import serializers
from .models import Libro , Categoria


class LibroSerializador(serializers.ModelSerializer):
    nombre_categoria = serializers.StringRelatedField(source="categoria")
    imagen_url = serializers.SerializerMethodField()

    class Meta:
        model = Libro
        fields = [
            "id",
            "titulo",
            "autor",
            "categoria",
            "nombre_categoria",
            "disponible",
            "prestado_a",
            "fecha_prestamo",
            "imagen_url",
            "imagen"
        ]

    def get_imagen_url(self, obj):
        request = self.context.get("request")
        if obj.imagen:
            if request is not None:
                return request.build_absolute_uri(obj.imagen.url)
            return obj.imagen.url
        return None

class CategoriaSerializador(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'