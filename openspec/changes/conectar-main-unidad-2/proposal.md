# Proposal

## Why

El `main.py` de la nueva carpeta de Unidad 2 solo crea la ventana de Tkinter y deja pendiente la conexión del modelo, la vista y el controlador. Además, los módulos existentes no pueden importarse ni conectar con MySQL de forma funcional por referencias faltantes y una configuración incompleta, por lo que la aplicación no puede iniciar el flujo de login y registro.

## What Changes

- Conectar el arranque de `main.py` con la vista de login, el modelo de usuarios y el controlador de autenticación.
- Completar las importaciones y dependencias entre vistas, controlador, modelo y conexión de base de datos.
- Corregir la creación de la conexión MySQL para usar la configuración de credenciales existente, reportar errores y permitir que las operaciones de autenticación continúen funcionando.
- Mantener el flujo actual de interfaz: login, apertura de registro, validaciones, mensajes y cierre ordenado de la aplicación.
- Verificar que la aplicación pueda importarse y arrancar desde `Unidad 2/Nueva carpeta` sin errores de nombres o rutas.

## Capabilities

### New Capabilities

- `unidad-2-login-flow`: Arranque de la aplicación y conexión funcional entre la interfaz Tkinter, el controlador de autenticación, el modelo de usuarios y la base de datos MySQL.

### Modified Capabilities

- Ninguna.

## Impact

- Afecta `Unidad 2/Nueva carpeta/main.py` y los módulos Python relacionados de esa carpeta (`conexion.py`, `inicio_sesión.py`, `registro.py`, `style.py` y `style1.py`).
- Requiere que el entorno tenga disponible el conector de MySQL y una base de datos `login_mvc` con la tabla `users` esperada por el modelo.
- No cambia el contrato visible del flujo de login y registro; habilita el comportamiento que ya está representado por los botones y métodos existentes.
