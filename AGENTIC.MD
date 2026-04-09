# AGENTIC

## Objetivo general
Desarrollar un sistema simple para bibliotecas que permita registrar libros, listar el catálogo, gestionar préstamos y devoluciones, y ejecutar la aplicación de forma containerizada con Docker.

## Alcance inicial (MVP)
- Registro de libros con título, autor y estado de disponibilidad.
- Listado de todos los libros.
- Préstamo de libros a un usuario.
- Devolución de libros.
- Interfaz REST simple para consumo desde frontend o pruebas.
- Ejecución en Docker para desarrollo y despliegue local.

## Requisitos principales
- Lenguaje: Python 3 con Flask para una API ligera.
- Persistencia inicial: almacenamiento en memoria para la primera versión.
- Contenedor Docker que permita desplegar la aplicación con un solo comando.
- Repositorio Git con commits claros y `.gitignore` apropiado.

## Funcionalidades del sistema
1. Vista de bienvenida y estado del servicio.
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
- Backend: API REST con Flask.
- Datos: almacenamiento en memoria con una lista de libros durante el desarrollo.
- Contenerización: `Dockerfile` sencillo para empaquetar la aplicación.
- Escalado futuro: migración a base de datos SQLite o PostgreSQL si se requiere persistencia.

## Estructura del proyecto
- `app.py`: aplicación Flask principal.
- `requirements.txt`: dependencias de Python.
- `Dockerfile`: define la imagen Docker.
- `.dockerignore`: archivos excluidos de la imagen Docker.
- `.gitignore`: archivos ignorados por Git.
- `README.md`: instrucciones básicas de uso.

## Dockerización
- Construir la imagen local con `docker build -t biblioteca-simple .`
- Ejecutar el contenedor con `docker run -p 5000:5000 biblioteca-simple`
- La API quedará disponible en `http://localhost:5000`

## Flujo Git inicial
1. `git init`
2. Crear `main` con los archivos base.
3. Añadir `.gitignore` y `Dockerfile`.
4. Hacer commit con mensaje claro: "Init simple library system with Docker config".

## Fases de desarrollo
1. Preparar el repositorio y la estructura base.
2. Implementar API básica en Flask.
3. Añadir Dockerfile y `.dockerignore`.
4. Probar localmente y en contenedor.
5. Documentar el uso en `README.md`.

## Extensiones futuras
- Persistencia con base de datos.
- Autenticación de usuarios.
- Frontend web con HTML/CSS/JS o React.
- Búsqueda y filtrado de libros.
- Gestión de categorías y reservas.
