# AGENTIC

## Objetivo general
Desarrollar un sistema simple para bibliotecas usando Django REST Framework que permita registrar libros, listar el catálogo, gestionar préstamos y devoluciones, y ejecutar la aplicación dentro de Docker.

## Alcance inicial (MVP)
- Registro de libros con título, autor y estado de disponibilidad.
- Listado de todos los libros.
- Préstamo de libros a un usuario.
- Devolución de libros.
- API REST con Django REST Framework.
- Persistencia local con SQLite.
- Ejecución en Docker para desarrollo y despliegue local.

## Requisitos principales
- Lenguaje: Python 3 con Django y Django REST Framework.
- Persistencia inicial: SQLite.
- Contenedor Docker que permita arrancar la aplicación con un solo comando.
- Repositorio Git con commits claros y `.gitignore` apropiado.

## Funcionalidades del sistema
1. Vista de estado del servicio.
2. Endpoint para listar libros.
3. Endpoint para crear nuevos libros.
4. Endpoint para consultar un libro por ID.
5. Endpoint para prestar un libro.
6. Endpoint para devolver un libro.

## Historia de usuario
- Como bibliotecario, quiero registrar nuevos libros para tener un catálogo actualizado.
- Como bibliotecario, quiero ver todos los libros disponibles para consultar el stock.
- Como bibliotecario, quiero prestar un libro y marcarlo como no disponible.
- Como bibliotecario, quiero devolver un libro y restaurar su disponibilidad.
- Como desarrollador, quiero ejecutar la aplicación dentro de un contenedor Docker.

## Arquitectura propuesta
- Backend: API REST con Django y Django REST Framework.
- Datos: SQLite para persistencia local.
- Contenerización: `Dockerfile` sencillo para empaquetar la aplicación.
- Escalado futuro: migración a otra base de datos y autenticación.

## Estructura del proyecto
- `manage.py`: comando de gestión de Django.
- `biblioteca/`: configuración del proyecto Django.
- `library/`: aplicación Django con el API de libros.
- `requirements.txt`: dependencias de Python.
- `Dockerfile`: define la imagen Docker.
- `.dockerignore`: archivos excluidos de la imagen Docker.
- `.gitignore`: archivos ignorados por Git.
- `README.md`: instrucciones básicas de uso.

## Dockerización
- Construir la imagen local con `docker build -t biblioteca-simple .`
- Ejecutar el contenedor con `docker run -p 8000:8000 biblioteca-simple`
- La API quedará disponible en `http://localhost:8000`

## Fases de desarrollo
1. Preparar el repositorio y la estructura base.
2. Implementar la API con Django REST Framework.
3. Añadir Dockerfile y `.dockerignore`.
4. Probar localmente y en contenedor.
5. Documentar el uso en `README.md`.

## Extensiones futuras
- Autenticación y permisos.
- Interfaz web o dashboard React.
- Búsqueda y filtrado de libros.
- Gestión de usuarios y reservas.
