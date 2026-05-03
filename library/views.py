from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import CategoriaFormulario, LibroFormulario
from .models import Libro, Categoria
from .serializers import LibroSerializador


class InicioVista(TemplateView):
    template_name = "library/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["libro_count"] = Libro.objects.count()
        context["categoria_count"] = Categoria.objects.count()
        context["libros"] = Libro.objects.all().order_by("titulo")[:12]
        context["categorias"] = Categoria.objects.all()
        return context


class LibroListaVista(LoginRequiredMixin, ListView):
    model = Libro
    template_name = "library/book_list.html"
    context_object_name = "libros"
    login_url = "iniciar-sesion"


class LibroCrearVista(LoginRequiredMixin, CreateView):
    model = Libro
    form_class = LibroFormulario
    template_name = "library/book_form.html"
    success_url = reverse_lazy("libro-lista-html")
    login_url = "iniciar-sesion"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Agregar libro"
        return context


class LibroDetalleVista(LoginRequiredMixin, DetailView):
    model = Libro
    template_name = "library/book_detail.html"
    context_object_name = "book"
    login_url = "iniciar-sesion"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        action = request.POST.get("action")

        if action == "loan":
            user = request.POST.get("user")
            if user:
                self.object.disponible = False
                self.object.prestado_a = user
                self.object.fecha_prestamo = timezone.now()
                self.object.save()
        elif action == "return":
            self.object.disponible = True
            self.object.prestado_a = None
            self.object.fecha_prestamo = None
            self.object.save()

        return redirect("libro-detalle-html", pk=self.object.pk)


class LibroEditarVista(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = LibroFormulario
    template_name = "library/book_form.html"
    success_url = reverse_lazy("libro-lista-html")
    login_url = "iniciar-sesion"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar libro"
        return context


class LibroEliminarVista(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "library/book_confirm_delete.html"
    success_url = reverse_lazy("libro-lista-html")
    login_url = "iniciar-sesion"


def cerrar_sesion(request):
    logout(request)
    return redirect("iniciar-sesion")


class CategoriaListaVista(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = "library/category_list.html"
    context_object_name = "categorias"
    login_url = "iniciar-sesion"


class CategoriaCrearVista(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaFormulario
    template_name = "library/category_form.html"
    success_url = reverse_lazy("categoria-lista-html")
    login_url = "iniciar-sesion"


class CategoriaEditarVista(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaFormulario
    template_name = "library/category_form.html"
    success_url = reverse_lazy("categoria-lista-html")
    login_url = "iniciar-sesion"


class CategoriaEliminarVista(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = "library/category_confirm_delete.html"
    success_url = reverse_lazy("categoria-lista-html")
    login_url = "iniciar-sesion"


class EstadoAPIView(APIView):
    def get(self, request):
        return Response({"message": "Biblioteca DRF lista", "libros": Libro.objects.count()})


class LibroListaCrearAPIView(generics.ListCreateAPIView):
    queryset = Libro.objects.all().order_by("id")
    serializer_class = LibroSerializador


class LibroDetalleAPIView(generics.RetrieveAPIView):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializador


class PrestamoLibroAPIView(APIView):
    def post(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        if not libro.disponible:
            return Response({"detail": "El libro ya está prestado."}, status=status.HTTP_400_BAD_REQUEST)

        usuario = request.data.get("user")
        if not usuario:
            return Response({"detail": "Se requiere el campo 'user'."}, status=status.HTTP_400_BAD_REQUEST)

        libro.disponible = False
        libro.prestado_a = usuario
        libro.fecha_prestamo = timezone.now()
        libro.save()
        return Response(LibroSerializador(libro).data)


class DevolucionLibroAPIView(APIView):
    def post(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)
        if libro.disponible:
            return Response({"detail": "El libro no está prestado."}, status=status.HTTP_400_BAD_REQUEST)

        libro.disponible = True
        libro.prestado_a = None
        libro.fecha_prestamo = None
        libro.save()
        return Response(LibroSerializador(libro).data)
