# Biblio

Biblio es una biblioteca digital sencilla construida con Django. Permite administrar libros, categorías e imágenes de forma local, con soporte para inicio de sesión y gestión desde una interfaz clara.

## Qué hace
- Muestra un catálogo de libros en la página de inicio
- Permite crear, editar y eliminar libros
- Permite crear, editar y eliminar categorías
- Genera imágenes opcionales para cada libro
- Mantiene los archivos de imagen en `media/book_images/`
- Usa SQLite para guardar los datos

## Rutas importantes
### Interfaz HTML
- `GET /` → catálogo y vista de biblioteca
- `GET /iniciar-sesion/` → iniciar sesión
- `GET /cerrar-sesion/` → cerrar sesión
- `GET /libros/` → lista de libros
- `GET /libros/agregar/` → agregar libro
- `GET /libros/<id>/` → detalle del libro
- `GET /libros/<id>/editar/` → editar libro
- `GET /libros/<id>/eliminar/` → eliminar libro
- `GET /categorias/` → lista de categorías
- `GET /categorias/agregar/` → agregar categoría
- `GET /categorias/<id>/editar/` → editar categoría
- `GET /categorias/<id>/eliminar/` → eliminar categoría

### Rutas para API
- `GET /api/` → estado del servicio
- `GET /api/libros/` → lista de libros
- `POST /api/libros/` → crear libro
- `GET /api/libros/<id>/` → obtener libro
- `POST /api/libros/<id>/prestar/` → prestar libro
- `POST /api/libros/<id>/devolver/` → devolver libro

## Cómo usar
1. Crear y activar el entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Instalar dependencias:
   ```bash
   python -m pip install -r requirements.txt
   ```
3. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```
4. Crear un usuario administrativo:
   ```bash
   python manage.py createsuperuser
   ```
5. Ejecutar el servidor:
   ```bash
   python manage.py runserver 0.0.0.0:8000
   ```

## Uso con Docker Compose
```bash
docker compose up --build
```

## Notas de implementación
- Las imágenes de libros se guardan en `media/book_images/`
- `media/` está montado en el contenedor Docker para persistencia local
- El proyecto usa `LOGIN_URL` y redirige a iniciar sesión después del cierre de sesión