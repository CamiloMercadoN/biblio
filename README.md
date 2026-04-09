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

### Endpoints
- `GET /api/` → estado del servicio
- `GET /api/books/` → lista de libros
- `POST /api/books/` → añadir libro
- `GET /api/books/<id>/` → obtener libro por id
- `POST /api/books/<id>/loan/` → prestar libro
- `POST /api/books/<id>/return/` → devolver libro

### Requisitos locales
- Python 3.14+
- `.venv` opcional para aislamiento

### Ejecución local
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

## Notas

La API usa SQLite para persistencia local y Django REST Framework para la capa de serialización y vistas.
