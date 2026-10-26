# Tasks

## 1. Preparar el archivo SQL importable

- [x] 1.1 Crear o consolidar `Unidad 2/Nueva carpeta/database_schema.sql` con la creación idempotente de `login_mvc` y `users`; verificar que el archivo contenga las cuatro columnas requeridas por el modelo. El esquema incluye `id`, `nombre`, `email` y `password`.
- [x] 1.2 Añadir las restricciones de clave primaria, incremento automático y correo único; verificar que una segunda importación no incluya instrucciones destructivas. El archivo usa `IF NOT EXISTS`, clave primaria, `AUTO_INCREMENT` y `UNIQUE`; no contiene `DROP`.

## 2. Documentar la importación

- [x] 2.1 Actualizar el README de Unidad 2 con el comando de importación desde consola y la alternativa de MySQL Workbench; verificar que las rutas y el nombre del archivo coincidan. La documentación cubre ambos métodos y referencia `database_schema.sql`.
- [x] 2.2 Validar el cambio OpenSpec en modo estricto y revisar el SQL final para confirmar que no contiene credenciales ni datos de prueba. La validación pasó y la revisión confirmó que no hay instrucciones destructivas, credenciales ni datos semilla.

## Workflow follow-up

- Importar el archivo en una instalación MySQL con permisos suficientes.
- Confirmar la creación de `login_mvc.users` antes de ejecutar la aplicación.
