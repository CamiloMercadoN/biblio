from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=120, unique=True)

    class Meta:
        verbose_name_plural = "categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="libros",
    )
    imagen = models.ImageField(upload_to="imagenes_libros/", blank=True, null=True)
    disponible = models.BooleanField(default=True)
    prestado_a = models.CharField(max_length=255, blank=True, null=True)
    fecha_prestamo = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.titulo} por {self.autor}"
