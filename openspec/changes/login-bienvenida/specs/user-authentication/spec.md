# Spec Delta

## Purpose

Define el comportamiento de autenticación de LAB7 y la transición desde el formulario de acceso a la ventana de bienvenida tras validar una cuenta.

## ADDED Requirements

### Requirement: Authenticate submitted credentials
The system SHALL verify the submitted username and password against the configured account store before granting access.

#### Scenario: Valid credentials
- **WHEN** the user submits credentials that match an account
- **THEN** the system grants access and opens the welcome window

#### Scenario: Invalid credentials
- **WHEN** the user submits credentials that do not match an account
- **THEN** the system denies access, displays an error, and keeps the login window available

### Requirement: Handle authentication service failures
The system SHALL report an authentication service failure without granting access when the account store cannot be reached or queried.

#### Scenario: Database unavailable
- **WHEN** the user submits credentials and the account store operation fails
- **THEN** the system displays a connection or service error and does not open the welcome window
