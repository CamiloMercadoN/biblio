<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import include, path
=======
from django.contrib.auth import views as auth_views
from django.urls import path
>>>>>>> upstream/main
from .views import (
    CategoriaCrearVista,
    CategoriaEliminarVista,
    CategoriaEditarVista,
    CategoriaListaVista,
    InicioVista,
    LibroCrearVista,
    LibroDetalleVista,
    LibroEditarVista,
    LibroEliminarVista,
    LibroListaVista,
    cerrar_sesion,
)

urlpatterns = [
    path("", InicioVista.as_view(), name="inicio"),
    path("iniciar-sesion/", auth_views.LoginView.as_view(template_name="library/login.html"), name="iniciar-sesion"),
    path("cerrar-sesion/", cerrar_sesion, name="cerrar-sesion"),
    path("libros/", LibroListaVista.as_view(), name="libro-lista-html"),
    path("libros/agregar/", LibroCrearVista.as_view(), name="libro-agregar-html"),
    path("libros/<int:pk>/", LibroDetalleVista.as_view(), name="libro-detalle-html"),
    path("libros/<int:pk>/editar/", LibroEditarVista.as_view(), name="libro-editar-html"),
    path("libros/<int:pk>/eliminar/", LibroEliminarVista.as_view(), name="libro-eliminar-html"),
    path("categorias/", CategoriaListaVista.as_view(), name="categoria-lista-html"),
    path("categorias/agregar/", CategoriaCrearVista.as_view(), name="categoria-agregar-html"),
    path("categorias/<int:pk>/editar/", CategoriaEditarVista.as_view(), name="categoria-editar-html"),
    path("categorias/<int:pk>/eliminar/", CategoriaEliminarVista.as_view(), name="categoria-eliminar-html"),
<<<<<<< HEAD

    path("api/", include("library.api_urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
]
>>>>>>> upstream/main
