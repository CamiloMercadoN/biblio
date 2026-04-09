# Biblio

Biblio es una biblioteca digital sencilla construida con Django. Permite administrar libros, categorías e imágenes de forma local, con soporte para login y gestión desde una interfaz clara.

## Qué hace
- Muestra un catálogo de libros en la página de inicio
- Permite crear, editar y eliminar libros
- Permite crear, editar y eliminar categorías
- Genera imágenes opcionales para cada libro
- Mantiene los archivos de imagen en `media/book_images/`
- Usa SQLite para guardar los datos

## Rutas importantes
### Interfaz HTML
- `GET /` → catálago y vista de biblioteca
- `GET /login/` → iniciar sesión
- `GET /logout/` → cerrar sesión
- `GET /books/` → lista de libros
- `GET /books/add/` → agregar libro
- `GET /books/<id>/` → detalle del libro
- `GET /books/<id>/edit/` → editar libro
- `GET /books/<id>/delete/` → eliminar libro
- `GET /categories/` → lista de categorías
- `GET /categories/add/` → agregar categoría
- `GET /categories/<id>/edit/` → editar categoría
- `GET /categories/<id>/delete/` → eliminar categoría

### Rutas para API
- `GET /api/` → estado del servicio
- `GET /api/books/` → lista de libros
- `POST /api/books/` → crear libro
- `GET /api/books/<id>/` → obtener libro
- `POST /api/books/<id>/loan/` → prestar libro
- `POST /api/books/<id>/return/` → devolver libro

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
- El proyecto usa `LOGIN_URL` y redirige al login después del logout
