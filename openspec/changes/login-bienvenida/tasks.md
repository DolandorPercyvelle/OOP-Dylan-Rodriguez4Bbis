# Tasks

## 1. Conexión y contrato de cuentas

- [x] 1.1 Completar la configuración MySQL sin incluir credenciales privadas en el código y verificar que la conexión se abre y se cierra correctamente con la configuración indicada.
- [x] 1.2 Definir en `database_squema.sql` la tabla y los campos de cuenta que usará el modelo, incluyendo verificador de contraseña; verificar que el script crea el esquema esperado en MySQL.

## 2. Autenticación

- [x] 2.1 Implementar en `login_model.py` la consulta parametrizada de cuentas y la comprobación del verificador de contraseña; verificar una cuenta válida y una inválida contra el esquema; migrar verificadores heredados de texto plano tras un acceso correcto.
- [x] 2.2 Propagar resultados distintos para credenciales inválidas y fallo de conexión/consulta sin filtrar detalles internos al mensaje de interfaz; verificar el mapeo de errores y los mensajes en el flujo implementado.

## 3. Flujo de interfaz

- [x] 3.1 Completar el formulario y la acción de login en `login_view.py`, conectándolos al modelo; verificar que ambos campos se envían al pulsar Login.
- [x] 3.2 Completar `home_view.py` y enlazarlo con el resultado exitoso para reutilizar la raíz Tk; comprobar en el flujo que no se crea un segundo bucle Tk.
- [x] 3.3 Mostrar errores de acceso o servicio y conservar el login ante fallos; comprobar en el flujo que la bienvenida solo se crea tras autenticación correcta.

## 4. Integración

- [x] 4.1 Ejecutar la aplicación configurada y recorrer manualmente login válido, credenciales inválidas y base de datos no disponible; verificar la ventana o mensaje correspondiente en cada caso.
