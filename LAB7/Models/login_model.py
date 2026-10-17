import hashlib
import hmac
import secrets

from Controller.database_connection import (
    DatabaseConnectionError,
    create_connection,
)


PBKDF2_ITERATIONS = 600_000


class AuthenticationServiceError(Exception):
    """Raised when the account store cannot complete an authentication query."""


def verify_password(password, stored_hash):
    try:
        algorithm, iterations, salt, expected = stored_hash.split("$", 3)
        if algorithm != "pbkdf2_sha256":
            return False
        actual = hashlib.pbkdf2_hmac(
            "sha256", password.encode("utf-8"), bytes.fromhex(salt), int(iterations)
        ).hex()
    except (AttributeError, TypeError, ValueError):
        return False
    return hmac.compare_digest(actual, expected)


def hash_password(password):
    salt = secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256", password.encode("utf-8"), salt, PBKDF2_ITERATIONS
    ).hex()
    return f"pbkdf2_sha256${PBKDF2_ITERATIONS}${salt.hex()}${digest}"


def authenticate(username, password):
    if not username or not password:
        return False

    connection = None
    cursor = None
    try:
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT password_hash FROM users WHERE username = %s LIMIT 1",
            (username.strip(),),
        )
        row = cursor.fetchone()
        if row is None:
            return False

        stored_hash = row[0]
        if isinstance(stored_hash, str) and stored_hash.startswith("pbkdf2_sha256$"):
            return verify_password(password, stored_hash)

        # Upgrade credentials created by earlier LAB7 versions that stored plaintext.
        if isinstance(stored_hash, str) and "$" not in stored_hash:
            if not hmac.compare_digest(
                stored_hash.encode("utf-8"), password.encode("utf-8")
            ):
                return False

            cursor.execute(
                "UPDATE users SET password_hash = %s WHERE username = %s AND password_hash = %s",
                (hash_password(password), username.strip(), stored_hash),
            )
            connection.commit()
            return True

        return False
    except Exception as exc:
        raise AuthenticationServiceError from exc
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

