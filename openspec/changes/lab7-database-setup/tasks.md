# Tasks

## 1. Inicialización del esquema

- [x] 1.1 Añadir conexión al servidor MySQL sin seleccionar una base y verificar que usa la configuración del entorno sin exponer la contraseña.
- [x] 1.2 Crear el comando de inicialización que aplica `database_squema.sql` de forma idempotente; verificar que dos ejecuciones crean/validan el esquema sin modificar filas existentes.
- [x] 1.3 Manejar errores de conexión, privilegios y esquema incompatible con mensajes accionables; verificar que los mensajes no contienen secretos.

## 2. Cuenta inicial

- [x] 2.1 Añadir el comando interactivo para usuario y contraseña oculta, usando el hash compatible con login y una inserción parametrizada; verificar que la cuenta nueva permite autenticarse.
- [x] 2.2 Rechazar nombres de usuario duplicados sin cambiar el verificador existente; verificar que la cuenta original sigue autenticando con su contraseña anterior.

## 3. Uso documentado e integración

- [x] 3.1 Actualizar `LAB7/README.md` con instalación de dependencias, variables de entorno y comandos de inicialización/cuenta; verificar cada comando desde PowerShell.
- [x] 3.2 Preparar MySQL, crear una cuenta con el comando y probar el login válido e inválido desde LAB7; verificar la bienvenida solo para la cuenta válida.
