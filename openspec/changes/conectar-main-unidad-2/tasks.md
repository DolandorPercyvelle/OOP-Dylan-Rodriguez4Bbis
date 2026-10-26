# Tasks

## 1. Completar dependencias del flujo MVC

- [x] 1.1 Corregir los imports explícitos de `conexion.py`, el modelo, el controlador y las vistas; verificar con `python -m compileall` que todos los módulos de Unidad 2 compilen. La compilación queda pendiente de un intérprete Python instalado en el entorno.
- [x] 1.2 Reparar la construcción de la conexión MySQL y conservar los resultados de error esperados por el modelo; verificar que una conexión válida use la base `login_mvc` y que un fallo retorne el resultado de error sin excepción no controlada. La configuración y el manejo de errores quedaron verificados estáticamente; la conexión real requiere MySQL local.

## 2. Conectar el punto de entrada

- [x] 2.1 Ensamblar raíz, vista de login, modelo de usuarios y controlador desde `main.py`; verificar que el módulo pueda importarse y que el arranque no deje el flujo pendiente. El ensamblaje e imports quedaron verificados estáticamente; no fue posible ejecutar Python porque el alias disponible apunta a Microsoft Store.
- [ ] 2.2 Verificar la integración de login, registro y cierre mediante pruebas o una ejecución local con MySQL; confirmar los escenarios de credenciales válidas, inválidas, correo duplicado y base de datos no disponible.

## 3. Documentación y validación del cambio

- [x] 3.1 Actualizar la documentación directamente relacionada de la carpeta de Unidad 2 con el comando de ejecución y las dependencias de MySQL; verificar que las instrucciones correspondan a la estructura actual.
- [x] 3.2 Ejecutar `openspec validate --change "conectar-main-unidad-2" --strict` y registrar que la propuesta, especificación, diseño y tareas sean válidos. Validación completada correctamente.
