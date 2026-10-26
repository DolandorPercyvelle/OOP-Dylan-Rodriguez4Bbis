# Design

## Context

La carpeta `Unidad 2/Nueva carpeta` contiene una vista de login, una vista de registro, un controlador de autenticación y un modelo de usuarios, pero `main.py` solo crea `Tk()` y deja el ensamblaje pendiente. También hay referencias a `tk`, `messagebox`, `RegisterView`, `Conexion`, `mysql.connector` y otros símbolos que no están disponibles en todos los módulos, y la configuración de la conexión contiene una línea inválida.

## Goals / Non-Goals

**Goals:**

- Crear una composición MVC explícita desde el punto de entrada.
- Hacer que todos los módulos puedan importarse desde la carpeta de la aplicación.
- Mantener los mensajes, validaciones y resultados actuales del login y registro.
- Gestionar conexiones y cursores sin dejar recursos abiertos cuando una operación termina.

**Non-Goals:**

- Rediseñar las ventanas o cambiar el flujo visible de usuario.
- Migrar a otro motor de base de datos.
- Implementar hash de contraseñas o una cuenta de configuración externa en este cambio.

## Decisions

- **El ensamblaje vive en `main.py`**: se creará la raíz, se instanciará `LoginView`, `UserModel` y `Authentication`, y finalmente se ejecutará el bucle principal. Esto mantiene el controlador independiente del arranque y evita lógica de composición distribuida.
- **Las dependencias se importan explícitamente por módulo**: cada vista importará las utilidades Tkinter que usa, el controlador importará sus vistas y utilidades, y el modelo importará su conexión y el conector MySQL. Se elige esta opción sobre depender de imports implícitos para que el programa sea ejecutable desde un entorno limpio.
- **La conexión conserva la configuración local actual**: `Conexion` será la única responsable de construir la conexión usando host, usuario, contraseña y base de datos. Se mantendrá el retorno `None` ante un error para que el modelo traduzca la indisponibilidad a sus resultados existentes.
- **Se validará por importación y pruebas de flujo sin interfaz interactiva**: se comprobará que los módulos compilen/importen y que el ensamblaje use las dependencias correctas; las operaciones reales de MySQL dependerán de que el servicio y el esquema estén disponibles localmente.

## Risks / Trade-offs

- **[Riesgo]** Las credenciales locales o el servidor MySQL pueden no estar disponibles. **Mitigación:** conservar el manejo explícito de errores y documentar la dependencia de `login_mvc`.
- **[Riesgo]** Las vistas actuales dependen de nombres globales de Tkinter. **Mitigación:** importar explícitamente `tk` y `messagebox` donde se utilizan y verificar la compilación de todos los módulos.
- **[Riesgo]** Las contraseñas siguen almacenándose como texto plano, porque cambiarlo alteraría el contrato de datos. **Mitigación:** dejarlo fuera de este cambio y tratarlo como una mejora de seguridad independiente.

## Migration Plan

1. Corregir imports y conexión en la carpeta de Unidad 2.
2. Conectar las instancias desde `main.py`.
3. Ejecutar validaciones de sintaxis/importación y, si existe el servicio local, probar login y registro.
4. Revertir los cambios de los módulos de Unidad 2 si el arranque o las pruebas de compatibilidad fallan.
