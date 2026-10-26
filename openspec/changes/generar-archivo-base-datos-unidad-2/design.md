# Design

## Context

La aplicación de Unidad 2 realiza consultas contra `login_mvc.users` y espera las columnas `id`, `nombre`, `email` y `password`. El proyecto ya contiene un archivo `database_schema.sql` en la carpeta de la aplicación, pero este cambio formaliza su contenido y la forma de importarlo.

## Goals / Non-Goals

**Goals:**

- Entregar un único archivo SQL portable para inicializar el esquema.
- Hacer que la importación sea segura para instalaciones nuevas y repetible sobre instalaciones existentes.
- Mantener los nombres y tipos compatibles con las consultas actuales del modelo.

**Non-Goals:**

- Crear usuarios de ejemplo o insertar contraseñas predeterminadas.
- Crear cuentas MySQL, permisos o credenciales del servidor.
- Ejecutar la importación automáticamente desde Python.
- Cambiar la autenticación o el almacenamiento de contraseñas.

## Decisions

- **Usar `CREATE DATABASE IF NOT EXISTS` y `CREATE TABLE IF NOT EXISTS`**: permite importar el archivo más de una vez sin borrar datos. Un script destructivo con `DROP TABLE` se descarta para evitar pérdida de cuentas.
- **Mantener `email` como clave única**: el controlador ya traduce conflictos de integridad a un resultado de correo duplicado; la restricción en la base garantiza esa regla aunque se inserte fuera de la interfaz.
- **Usar `utf8mb4`**: permite nombres y datos internacionales sin modificar el contrato de las consultas.
- **No incluir datos semilla**: evita introducir credenciales conocidas y deja el registro de usuarios bajo control del operador.

## Risks / Trade-offs

- **[Riesgo]** El usuario MySQL puede no tener permisos para crear bases. → La documentación indicará que la importación requiere privilegios suficientes.
- **[Riesgo]** Una tabla existente con columnas incompatibles no se corrige automáticamente. → El script no destruye datos; la incompatibilidad debe revisarse antes de migrar.
- **[Riesgo]** Las contraseñas se almacenan según el modelo actual. → El hash de contraseñas queda fuera de este cambio para no romper el contrato existente.

## Migration Plan

1. Importar el archivo SQL desde MySQL Workbench o la consola.
2. Confirmar que existe `login_mvc.users` con las columnas esperadas.
3. Ejecutar la aplicación de Unidad 2 y probar registro/login.
4. Si el esquema existente es incompatible, respaldar los datos y aplicar una migración explícita; no eliminar la tabla automáticamente.
