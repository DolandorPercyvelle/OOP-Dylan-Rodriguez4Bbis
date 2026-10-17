# Proposal

## Why

LAB7 ya tiene un esquema SQL para `lab7.users`, pero preparar la base y crear una cuenta inicial requiere pasos manuales que pueden fallar o almacenar contraseñas de forma insegura. Un flujo de preparación reproducible permitirá dejar MySQL listo para usar con el login.

## What Changes

- Añadir un comando de preparación que cree la base `lab7` y la tabla de usuarios a partir del esquema del proyecto en una instancia MySQL existente.
- Añadir una operación de configuración inicial que solicite usuario y contraseña de forma interactiva y guarde únicamente el verificador compatible con el login.
- Hacer que la preparación sea repetible y que no reemplace cuentas existentes ni revele contraseñas o secretos de conexión.
- Documentar los requisitos de MySQL, configuración y comandos para preparar y ejecutar LAB7.

## Capabilities

### New Capabilities
- `database-provisioning`: preparar de forma reproducible el esquema de LAB7 y una cuenta inicial para que el login pueda utilizarse.

### Modified Capabilities

## Impact

- Esquema SQL: `LAB7/Models/database_squema.sql`.
- Configuración y conexión: `LAB7/Controller/config.py` y `LAB7/Controller/database_connection.py`.
- Modelo de cuentas y contraseña: `LAB7/Models/login_model.py`.
- Nuevo comando de preparación y documentación de `LAB7`.
- Requiere un servidor MySQL existente y privilegios para crear la base y la tabla; no instala ni administra el servidor.
