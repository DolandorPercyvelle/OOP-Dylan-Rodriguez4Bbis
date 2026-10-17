# Spec Delta

## Purpose

Provide a repeatable way to prepare LAB7's MySQL schema and create its first usable account without storing plaintext passwords or overwriting existing users.

## ADDED Requirements

### Requirement: Initialize the LAB7 database schema
The system SHALL create the LAB7 database and required users table on a configured MySQL server, and repeated initialization SHALL preserve existing account data.

#### Scenario: First initialization
- **WHEN** an operator initializes LAB7 against a MySQL server with sufficient privileges
- **THEN** the `lab7` database and the `users` table required by login are created

#### Scenario: Repeated initialization
- **WHEN** an operator initializes LAB7 after the schema already exists
- **THEN** the operation completes without deleting or changing existing users

#### Scenario: MySQL unavailable or privileges insufficient
- **WHEN** initialization cannot connect to MySQL or cannot create the schema
- **THEN** the command reports failure without printing connection secrets

### Requirement: Provision an initial LAB7 account
The system SHALL allow an operator to create an account for login using an interactively entered password stored only as a verifier compatible with LAB7 authentication.

#### Scenario: Create account
- **WHEN** an operator provides a new username and password during setup
- **THEN** the account is stored with a password verifier and can be used by the login flow

#### Scenario: Username already exists
- **WHEN** an operator attempts to provision a username that already exists
- **THEN** the existing account remains unchanged and the command reports that no account was created

#### Scenario: Password entry
- **WHEN** an operator enters the password during provisioning
- **THEN** the password is not echoed to the terminal or written to application logs
