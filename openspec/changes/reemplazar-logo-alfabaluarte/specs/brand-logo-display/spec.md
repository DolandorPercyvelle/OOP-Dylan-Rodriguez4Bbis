# Spec Delta

## Purpose

Esta capacidad define cómo el sistema presenta la identidad visual de Alfa Baluarte en su navegación principal, usando el logo oficial disponible en los assets de la aplicación.

## ADDED Requirements

### Requirement: La barra lateral debe mostrar el logo oficial
La barra lateral SHALL mostrar la imagen oficial de Alfa Baluarte en lugar del identificador textual "AB", manteniendo una escala legible y la composición visual del bloque de marca.

#### Scenario: Logo visible al iniciar el sistema
- **WHEN** la ventana principal se construye con el asset oficial disponible
- **THEN** el bloque de marca de la barra lateral muestra la imagen del logo y conserva el nombre "ALFA BALUARTE"

#### Scenario: Logo ausente o ilegible
- **WHEN** el asset configurado no está disponible o no puede ser leído
- **THEN** el sistema informa explícitamente el problema durante la construcción de la interfaz y no presenta un logo textual como sustituto silencioso
