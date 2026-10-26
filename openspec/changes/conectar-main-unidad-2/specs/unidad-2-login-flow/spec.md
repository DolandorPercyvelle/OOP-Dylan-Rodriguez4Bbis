# Spec Delta

## Purpose

Permite iniciar la aplicación de Unidad 2 con un flujo de autenticación conectado, de modo que la interfaz existente pueda validar usuarios y registrar cuentas mediante la base de datos configurada.

## ADDED Requirements

### Requirement: Application startup wires the authentication flow
The application SHALL start one login window and connect its login and registration actions to the authentication model and controller.

#### Scenario: Start application
- **WHEN** the user runs `main.py`
- **THEN** one login window is created and its controls are operational without import or name-resolution errors

#### Scenario: Close application
- **WHEN** the user closes the main window
- **THEN** the authentication flow performs its cleanup and the Tkinter application exits

### Requirement: Database-backed authentication operations
The system SHALL use the configured MySQL database to validate credentials and register users, returning the existing success, duplicate, or error outcomes to the interface.

#### Scenario: Valid login
- **WHEN** a user submits an email and password that match a database record
- **THEN** the interface reports successful access and clears the login fields

#### Scenario: Invalid login
- **WHEN** a user submits credentials that do not match a database record
- **THEN** the interface reports denied access without crashing

#### Scenario: New user registration
- **WHEN** a user submits valid registration data for an unused email
- **THEN** the record is stored and the registration window closes

#### Scenario: Database unavailable
- **WHEN** the database cannot be reached during login or registration
- **THEN** the interface receives an error outcome and reports that the operation could not be completed
