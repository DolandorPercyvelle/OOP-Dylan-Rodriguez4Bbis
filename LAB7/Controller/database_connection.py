from Controller.config import get_database_config, get_server_config


class DatabaseConnectionError(Exception):
    """Raised when MySQL cannot be reached or the driver is unavailable."""


def create_connection():
    try:
        import mysql.connector

        return mysql.connector.connect(**get_database_config())
    except Exception as exc:
        raise DatabaseConnectionError("No se pudo conectar con la base de datos.") from exc


def create_server_connection():
    try:
        import mysql.connector

        return mysql.connector.connect(**get_server_config())
    except Exception as exc:
        raise DatabaseConnectionError("No se pudo conectar con el servidor MySQL.") from exc
