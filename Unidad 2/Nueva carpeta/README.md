# Aplicación de login de Unidad 2

## Requisitos

- Python 3.
- MySQL Server en `localhost`.
- Base de datos `login_mvc` con la tabla `users` usada por el modelo.
- Paquete `mysql-connector-python`.

## Crear la base de datos

Con MySQL iniciado, ejecuta el esquema incluido:

```powershell
mysql -u root -p < database_schema.sql
```

Si tu usuario `root` no tiene contraseña, elimina `-p`. El esquema crea la
base `login_mvc` y la tabla `users` de forma segura si todavía no existen.

También puedes abrir `database_schema.sql` en MySQL Workbench, conectarte al
servidor local y pulsar el botón de ejecución. Después verifica en el panel
Schemas que aparezcan `login_mvc` y `login_mvc.users`.

## Ejecución

Desde esta carpeta, instala la dependencia y ejecuta:

```powershell
py -m pip install mysql-connector-python
py main.py
```

La conexión usa el usuario local `root` sin contraseña, la base `login_mvc` y
el host `localhost`. Si tu instalación de MySQL usa otros valores, actualiza
`conexion.py` antes de iniciar la aplicación.
