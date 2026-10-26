# Proposal

## Why

La aplicación de login de la Unidad 2 necesita que la base de datos y la tabla `users` puedan crearse fácilmente en una instalación MySQL nueva. Entregar un archivo SQL importable reduce errores de configuración y deja el esquema alineado con las consultas que ya utiliza el modelo.

## What Changes

- Entregar un archivo SQL autocontenido para crear la base `login_mvc`.
- Crear la tabla `users` con las columnas requeridas por el login y el registro.
- Incluir restricciones de clave primaria, incremento automático y correo único.
- Hacer que el script sea idempotente para poder importarlo sin fallar si la base o tabla ya existen.
- Documentar el comando de importación y la estructura creada.

## Capabilities

### New Capabilities

- `database-provisioning`: Provisión reproducible del esquema MySQL requerido por el login de Unidad 2 mediante un archivo SQL importable.

### Modified Capabilities

- Ninguna.

## Impact

- Añade o formaliza el archivo SQL de la carpeta `Unidad 2/Nueva carpeta`.
- Afecta la documentación de ejecución de esa aplicación.
- Requiere permisos MySQL para crear la base de datos y la tabla.
- No ejecuta comandos contra el servidor ni incluye credenciales.
