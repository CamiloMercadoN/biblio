# Biblioteca Simple

Este proyecto es un sistema básico para gestionar una biblioteca. Está construido con Django REST Framework y está preparado para ejecutarse dentro de Docker.

## Instrucciones

### Con Docker
1. Construir la imagen Docker:
   ```bash
   docker build -t biblioteca-simple .
   ```

2. Ejecutar el contenedor:
   ```bash
   docker run -p 8000:8000 biblioteca-simple
   ```

3. Acceder a la API en `http://localhost:8000`

### Endpoints HTML
- `GET /` → vista de inicio
- `GET /login/` → iniciar sesión
- `GET /logout/` → cerrar sesión
- `GET /books/` → catálogo de libros
- `GET /books/add/` → agregar libro
- `GET /books/<id>/` → detalle de libro, préstamo y devolución
- `GET /books/<id>/edit/` → editar libro
- `GET /books/<id>/delete/` → eliminar libro
- `GET /categories/` → catálogo de categorías
- `GET /categories/add/` → agregar categoría
- `GET /categories/<id>/edit/` → editar categoría
- `GET /categories/<id>/delete/` → eliminar categoría

### Imágenes
- Los libros pueden tener una imagen opcional.
- Las imágenes se guardan en `media/book_images/`.
- Docker Compose monta `./media` en el contenedor para persistencia local.

### Endpoints API
- `GET /api/` → estado del servicio
- `GET /api/books/` → lista de libros
- `POST /api/books/` → añadir libro
- `GET /api/books/<id>/` → obtener libro por id
- `POST /api/books/<id>/loan/` → prestar libro
- `POST /api/books/<id>/return/` → devolver libro

### Requisitos locales
- Python 3.14+
- `.venv` opcional para aislamiento

Para acceder al sistema, crea un usuario con:
```bash
python manage.py createsuperuser
```

### Ejecución local
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

### Ejecución con Docker Compose
Asegúrate de usar `compose` correctamente y no `ocmpose`.

```bash
docker compose up --build
```

Si quieres ejecutar en segundo plano:

```bash
docker compose up --build -d
```

## Notas

La API usa SQLite para persistencia local y Django REST Framework para la capa de serialización y vistas.
