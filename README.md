# Biblioteca Simple

Este proyecto es un sistema básico para gestionar una biblioteca. Está construido con Python y Flask y está preparado para ejecutarse dentro de Docker.

## Instrucciones

1. Construir la imagen Docker:
   ```bash
   docker build -t biblioteca-simple .
   ```

2. Ejecutar el contenedor:
   ```bash
   docker run -p 5000:5000 biblioteca-simple
   ```

3. Probar la API:
   - `GET /` → estado del servicio
   - `GET /books` → lista de libros
   - `POST /books` → añadir libro
   - `POST /books/<id>/loan` → prestar libro
   - `POST /books/<id>/return` → devolver libro

## Dependencias

- Flask

## Notas

Este repositorio es un punto de partida para un sistema de bibliotecas sencillo. Para producción, se recomienda añadir persistencia en base de datos y autenticación.
