# LAB7

## Requisitos

- Python 3.10 o posterior.
- MySQL instalado y en ejecucion. El inicializador crea la base y tabla, pero no instala ni arranca el servidor.
- Un usuario MySQL con permiso para crear bases y tablas.

## Preparar la base y la cuenta

Desde la raiz del proyecto, configura la conexion en PowerShell. No guardes contrasenas reales en el repositorio:

```powershell
$env:MYSQL_HOST = "127.0.0.1"
$env:MYSQL_PORT = "3306"
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = ""
$env:MYSQL_DATABASE = "lab7"
py -m pip install -r LAB7/requirements.txt
py LAB7/setup_database.py init
py LAB7/setup_database.py create-user
```

`create-user` solicita la contrasena dos veces sin mostrarla. El sistema guarda un verificador PBKDF2 compatible con el login. Si el usuario ya existe, no cambia su cuenta.

## Iniciar la aplicacion

```powershell
py LAB7/main.py
```
