import argparse
from getpass import getpass
from pathlib import Path

from Controller.database_connection import (
    create_connection,
    create_server_connection,
)
from Models.login_model import hash_password


class DatabaseSetupError(Exception):
    """Raised when the LAB7 schema cannot be initialized or verified."""


class UserAlreadyExistsError(DatabaseSetupError):
    """Raised when setup attempts to create an existing username."""


def create_user(username, password):
    username = username.strip()
    if not username or len(username) > 100:
        raise DatabaseSetupError("El usuario debe tener entre 1 y 100 caracteres.")
    if not password:
        raise DatabaseSetupError("La contrasena no puede estar vacia.")

    connection = None
    cursor = None
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
            (username, hash_password(password)),
        )
        connection.commit()
    except Exception as exc:
        if getattr(exc, "errno", None) == 1062:
            raise UserAlreadyExistsError(
                f"El usuario '{username}' ya existe; no se modifico su cuenta."
            ) from exc
        if connection is not None:
            try:
                connection.rollback()
            except Exception:
                pass
        raise DatabaseSetupError(
            "No se pudo crear la cuenta. Comprueba que la base LAB7 esta inicializada."
        ) from exc
    finally:
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if connection is not None:
            try:
                connection.close()
            except Exception:
                pass


def initialize_database():
    schema_path = Path(__file__).parent / "Models" / "database_squema.sql"
    try:
        schema = schema_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise DatabaseSetupError(
            "No se encontro o no se pudo leer Models/database_squema.sql."
        ) from exc

    connection = None
    cursor = None
    try:
        connection = create_server_connection()
        cursor = connection.cursor()
        cursor.execute(schema, map_results=True)
        while cursor.nextset():
            pass
    except Exception as exc:
        raise DatabaseSetupError(
            "No se pudo crear el esquema LAB7. Comprueba el servidor y los permisos MySQL."
        ) from exc
    finally:
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if connection is not None:
            try:
                connection.close()
            except Exception:
                pass

    connection = None
    cursor = None
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("SHOW COLUMNS FROM users")
        columns = {row[0] for row in cursor.fetchall()}
        required = {"username", "password_hash"}
        if not required.issubset(columns):
            missing = ", ".join(sorted(required - columns))
            raise DatabaseSetupError(
                f"La tabla users no coincide con LAB7; faltan las columnas: {missing}."
            )
    except DatabaseSetupError:
        raise
    except Exception as exc:
        raise DatabaseSetupError(
            "El esquema se ejecuto, pero no se pudo verificar la tabla users."
        ) from exc
    finally:
        if cursor is not None:
            try:
                cursor.close()
            except Exception:
                pass
        if connection is not None:
            try:
                connection.close()
            except Exception:
                pass


def main():
    parser = argparse.ArgumentParser(description="Preparacion de la base de datos LAB7")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("init", help="crear y verificar la base y la tabla users")
    commands.add_parser("create-user", help="crear una cuenta inicial de acceso")
    args = parser.parse_args()

    if args.command == "init":
        try:
            initialize_database()
        except DatabaseSetupError as exc:
            print(f"Error: {exc}")
            return 1
        print("Base de datos LAB7 lista.")
        return 0
    if args.command == "create-user":
        username = input("Usuario: ").strip()
        password = getpass("Contrasena: ")
        confirmation = getpass("Confirma la contrasena: ")
        if password != confirmation:
            print("Error: las contrasenas no coinciden.")
            return 1
        try:
            create_user(username, password)
        except DatabaseSetupError as exc:
            print(f"Error: {exc}")
            return 1
        print(f"Cuenta '{username}' creada.")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
