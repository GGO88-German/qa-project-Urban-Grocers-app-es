# Proyecto Urban Grocers

## Descripción

Este proyecto contiene pruebas automatizadas para la API de Urban Grocers.

El objetivo es comprobar el comportamiento del endpoint de creación de kits de productos, validando diferentes valores para el parámetro `name`.

Las pruebas crean primero un nuevo usuario para obtener un `authToken` y posteriormente utilizan ese token para crear un kit.

## Tecnologías utilizadas

- Python
- Pytest
- Requests
- Git
- GitHub
- Visual Studio Code

## Archivos del proyecto

- `configuration.py`: contiene la URL del servidor y las rutas de los endpoints.
- `data.py`: contiene los datos utilizados para crear usuarios y kits.
- `sender_stand_request.py`: contiene las funciones para enviar solicitudes HTTP a la API.
- `create_kit_name_kit_test.py`: contiene las pruebas automatizadas para validar el campo `name`.
- `.gitignore`: evita subir archivos temporales o innecesarios al repositorio.

## Casos de prueba

Se implementaron 9 casos de prueba para el parámetro `name`:

1. Nombre con 1 carácter.
2. Nombre con 511 caracteres.
3. Nombre con 0 caracteres.
4. Nombre con 512 caracteres.
5. Nombre con caracteres especiales.
6. Nombre con espacios.
7. Nombre con números.
8. Solicitud sin el parámetro `name`.
9. Parámetro `name` con un tipo de dato incorrecto (número).

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/GGO88-German/qa-project-Urban-Grocers-app-es.git