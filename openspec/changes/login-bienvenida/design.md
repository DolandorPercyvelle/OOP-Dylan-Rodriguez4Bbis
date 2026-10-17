# Design

## Context

`LAB7/Views/login_view.py`, `LAB7/Views/home_view.py`, `LAB7/Controller/database_connection.py`, and `LAB7/Controller/config.py` exist, but the login action is empty and the model only imports `mysql.connector`. The SQL schema file is present but does not currently define the account contract. See `proposal.md` and `specs/user-authentication/spec.md` for motivation and observable behavior.

## Goals / Non-Goals

**Goals:**
- Connect the existing Tkinter login flow to a reusable authentication model and MySQL connection.
- Keep view responsibilities focused on collecting input and showing outcomes.
- Ensure only a verified account opens the welcome view.

**Non-Goals:**
- Add account registration, password recovery, or role-based authorization.
- Replace Tkinter or MySQL with a different UI or persistence technology.

## Decisions

- Keep authentication in `login_model.py` and connection creation in `database_connection.py`; the view calls the model and handles the result. This follows the existing file boundaries and keeps database operations out of Tkinter event handlers.
- Read connection settings from `config.py` (or environment-backed settings) rather than embedding credentials in query code. Use parameterized SQL for credential lookups.
- Define or align the SQL account table with the fields the model queries. Store password verifiers rather than plaintext passwords; compare using a standard password hashing approach if the schema has no existing compatible authentication contract.
- Reuse the existing Tk root for the welcome screen after successful authentication, closing or replacing the login content. This avoids multiple independent Tk event loops; failed logins leave the login screen active.
- Represent authentication outcomes distinctly enough for the view to show invalid credentials separately from connection/query failures without exposing database details to the user.
- For an existing legacy account whose stored value is plain text, compare it safely and replace it with a PBKDF2 verifier only after a successful login. Failed attempts do not modify the account; unrecognized structured verifier formats fail closed.

## Risks / Trade-offs

- [MySQL service or account schema is not supplied by the repository] → Provide a documented schema and clear configuration inputs, and surface connection failures in the login view.
- [Credential handling may be incompatible with an existing database] → Reuse the established account format if one is provided at implementation time; otherwise create the matching schema and hashing contract together.
- [Database error details can expose internal configuration] → Show a concise user-facing error and keep technical detail out of the UI.

## Migration Plan

1. Configure the MySQL connection and create or align the account table using the SQL schema.
2. Start the application and verify invalid credentials, valid credentials, and unavailable-database behavior.
3. Roll back by restoring the prior LAB7 files; no existing account data needs migration unless an external schema is adopted.
