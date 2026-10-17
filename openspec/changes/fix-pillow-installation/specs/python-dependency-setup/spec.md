# Spec Delta

## Purpose

Provides a repeatable way to install the Python packages a lab needs before running it, so a clean environment can start the lab without missing dependency imports.

## ADDED Requirements

### Requirement: Labs declare runtime dependencies
Each lab that requires third-party Python packages MUST provide a dependency manifest and a documented command to install those packages using the Python interpreter intended to run the lab.

#### Scenario: Install dependencies for LAB7.1
- **WHEN** a user follows the documented setup from the repository root
- **THEN** the packages required by LAB7.1 are installed for the Python interpreter used to launch that lab

#### Scenario: Run LAB7.1 with dependencies installed
- **WHEN** a user launches LAB7.1 after completing its documented dependency installation
- **THEN** its image views can import Pillow without a missing `PIL` module error
