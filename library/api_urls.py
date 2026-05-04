<<<<<<< HEAD
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
=======
from django.urls import path
>>>>>>> upstream/main
from .views import (
    EstadoAPIView,
    LibroDetalleAPIView,
    LibroListaCrearAPIView,
    PrestamoLibroAPIView,
    DevolucionLibroAPIView,
)
<<<<<<< HEAD
from .api_views import LibroViewSet, CategoriaViewSet

router = DefaultRouter()
router.register(r'libros', LibroViewSet, basename='api-libro')
router.register(r'categorias', CategoriaViewSet, basename='api-categoria')

urlpatterns = [
    #path("", EstadoAPIView.as_view(), name="api-salud"),
    #path("libros/", LibroListaCrearAPIView.as_view(), name="api-libro-lista"),
    #path("libros/<int:pk>/", LibroDetalleAPIView.as_view(), name="api-libro-detalle"),
    #path("libros/<int:pk>/prestar/", PrestamoLibroAPIView.as_view(), name="api-libro-prestar"),
    #path("libros/<int:pk>/devolver/", DevolucionLibroAPIView.as_view(), name="api-libro-devolver"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
=======

urlpatterns = [
    path("", EstadoAPIView.as_view(), name="api-salud"),
    path("libros/", LibroListaCrearAPIView.as_view(), name="api-libro-lista"),
    path("libros/<int:pk>/", LibroDetalleAPIView.as_view(), name="api-libro-detalle"),
    path("libros/<int:pk>/prestar/", PrestamoLibroAPIView.as_view(), name="api-libro-prestar"),
    path("libros/<int:pk>/devolver/", DevolucionLibroAPIView.as_view(), name="api-libro-devolver"),
>>>>>>> upstream/main
]
