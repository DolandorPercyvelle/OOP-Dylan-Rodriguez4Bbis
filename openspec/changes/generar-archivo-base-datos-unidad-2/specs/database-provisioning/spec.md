# Spec Delta

## Purpose

Proporciona un esquema SQL reproducible para que la aplicación de login de Unidad 2 pueda inicializar su base de datos y comenzar a registrar y validar usuarios mediante MySQL.

## ADDED Requirements

### Requirement: Importable login database schema
The project SHALL provide an SQL script that creates the `login_mvc` database and the `users` table required by the Unit 2 login application.

#### Scenario: Import into a new MySQL server
- **WHEN** an administrator imports the script with sufficient database privileges
- **THEN** the `login_mvc` database and its `users` table are created with the columns `id`, `nombre`, `email`, and `password`

#### Scenario: Re-import an existing schema
- **WHEN** an administrator imports the script after the database and table already exist
- **THEN** the import completes without attempting to destroy existing user records

### Requirement: User identity constraints
The database schema SHALL enforce an auto-incrementing primary key and prevent duplicate email addresses.

#### Scenario: Register unique email
- **WHEN** a new user is inserted with an email not present in `users`
- **THEN** the insert is accepted and receives a generated numeric identifier

#### Scenario: Register duplicate email
- **WHEN** a new user is inserted with an email already present in `users`
- **THEN** MySQL rejects the insert through the email uniqueness constraint
