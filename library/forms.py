from django import forms
from .models import Libro, Categoria


class LibroFormulario(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["titulo", "autor", "categoria", "imagen"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control", "placeholder": "Título"}),
            "autor": forms.TextInput(attrs={"class": "form-control", "placeholder": "Autor"}),
            "categoria": forms.Select(attrs={"class": "form-control"}),
        }


class CategoriaFormulario(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre de categoría"}),
        }
