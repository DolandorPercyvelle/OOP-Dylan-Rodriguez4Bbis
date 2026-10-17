# Design

## Context

The login implementation expects a MySQL database named `lab7` with a `users(username, password_hash)` table. The checked-in SQL creates those objects, but the current README requires a separate MySQL client and manual account insertion. See `proposal.md` and `specs/database-provisioning/spec.md` for scope and behavior.

## Goals / Non-Goals

**Goals:**
- Prepare the existing MySQL server through a documented Python command.
- Create an initial account using the same password verifier as login.
- Keep setup separate from normal application startup and preserve existing rows.

**Non-Goals:**
- Install, start, or configure the MySQL server service itself.
- Add account registration to the Tkinter login UI or reset existing passwords.

## Decisions

- Add a setup command with separate schema-initialization and account-creation actions. The app continues to connect to the selected database at runtime; the setup action connects to the server without selecting `lab7` so it can create the database first.
- Keep `database_squema.sql` as the schema source of truth and apply it using MySQL Connector/Python. Initialization uses idempotent DDL and does not drop tables or rows.
- Reuse the password hashing format already used by `login_model.py`; prompt with a hidden terminal input and insert with parameterized SQL. Refuse duplicate usernames instead of changing their existing verifier.
- Read host, port, user, and password from the existing environment configuration. Setup reports actionable errors without printing the connection password or entered account password.
- Document required server privileges and the setup commands in `LAB7/README.md`; avoid requiring the `mysql` shell client.

## Risks / Trade-offs

- [The configured MySQL account lacks CREATE DATABASE privileges] → State the required privilege and report the database operation that failed.
- [Schema SQL and the setup command could drift] → Keep one checked-in schema file authoritative and verify setup against it.
- [An existing schema may have incompatible columns] → Do not alter or drop existing tables automatically; report the mismatch for deliberate repair.

## Migration Plan

1. Run the schema initialization command against the configured MySQL server.
2. Run the account creation command to provision a login user.
3. Start LAB7 and verify the new account can log in.

Existing `lab7.users` rows are retained. Rollback consists of removing the added setup command and documentation; the initializer does not require destructive rollback steps.
