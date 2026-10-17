# Proposal

## Why

El flujo de acceso de LAB7 está incompleto: la acción de autenticación no hace nada y el modelo, la conexión y las vistas todavía no coordinan el inicio de sesión. Se necesita un recorrido funcional que permita validar credenciales y mostrar la ventana de bienvenida al completar correctamente el login.

## What Changes

- Conectar la vista de login con el modelo de autenticación y la conexión MySQL configurada.
- Actualizar a PBKDF2 las contrase?as heredadas en texto plano solo despu?s de un acceso correcto.
- Validar las credenciales introducidas y distinguir acceso correcto, credenciales inválidas y fallos de conexión.
- Abrir la ventana de bienvenida después de un acceso correcto; mantener la ventana de login y mostrar un mensaje cuando el acceso falle.
- Completar el esquema de datos requerido para consultar las cuentas, o documentar la estructura esperada si ya se proporciona externamente.

## Capabilities

### New Capabilities
- `user-authentication`: autenticar credenciales con la base de datos y dirigir a la persona usuaria a la ventana de bienvenida tras un acceso correcto.

### Modified Capabilities

## Impact

- Vistas: `LAB7/Views/login_view.py` y `LAB7/Views/home_view.py`.
- Modelo: `LAB7/Models/login_model.py`.
- Acceso y configuración de base de datos: `LAB7/Controller/database_connection.py` y `LAB7/Controller/config.py`.
- Esquema: `LAB7/Models/database_squema.sql`.
- Dependencia externa: MySQL Connector/Python y una instancia MySQL configurada para la aplicación.
