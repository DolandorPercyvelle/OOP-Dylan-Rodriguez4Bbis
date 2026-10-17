import os


def get_database_config():
    """Build MySQL settings from the process environment."""
    config = get_server_config()
    config["database"] = os.getenv("MYSQL_DATABASE", "lab7")
    return config


def get_server_config():
    """Build MySQL settings without selecting a database."""
    return {
        "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
        "port": int(os.getenv("MYSQL_PORT", "3306")),
        "user": os.getenv("MYSQL_USER", "root"),
        "password": os.getenv("MYSQL_PASSWORD", ""),
    }
