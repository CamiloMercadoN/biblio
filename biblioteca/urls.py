"""
Configuración de URLs para el proyecto biblioteca.

La lista `urlpatterns` enlaza rutas con vistas. Más información en:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Ejemplos:
Vistas basadas en funciones
    1. Importar la vista:  from my_app import views
    2. Añadir una URL: path('', views.home, name='home')
Vistas basadas en clases
    1. Importar la vista:  from other_app.views import Home
    2. Añadir una URL: path('', Home.as_view(), name='home')
Incluir otro archivo de rutas
    1. Importar include(): from django.urls import include, path
    2. Añadir una URL: path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls')),
    path('api/', include('library.api_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
