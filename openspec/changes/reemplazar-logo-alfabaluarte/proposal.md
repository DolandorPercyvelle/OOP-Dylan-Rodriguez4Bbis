# Proposal

## Why

La barra lateral del sistema de Alfa Baluarte muestra actualmente las letras "AB" como identificador visual. Ya existe una imagen de marca en los assets del proyecto, por lo que usarla permitirá que la interfaz represente de forma consistente la identidad visual definida para el sistema.

## What Changes

- Reemplazar el bloque textual "AB" de la barra lateral por la imagen de logo ubicada en `sistema/src/assets/logo.png`.
- Mantener el nombre "ALFA BALUARTE", el subtítulo y la estructura de navegación existentes.
- Ajustar el tamaño y la presentación del logo para que conserve una apariencia adecuada dentro de la barra lateral sin alterar su distribución.
- Mantener un comportamiento explícito cuando el asset no pueda cargarse, evitando que la ventana falle silenciosamente.

## Capabilities

### New Capabilities

- `brand-logo-display`: Mostrar el logo de Alfa Baluarte desde el asset configurado en la identidad visual de la aplicación.

### Modified Capabilities

<!-- No existing capability specs cover this behavior. -->

## Impact

- Afecta el componente visual de la barra lateral en `Nueva carpeta/alfabaluarte/sistema/src/views/components/barra_lateral.py`.
- Usa el recurso existente `Nueva carpeta/alfabaluarte/sistema/src/assets/logo.png`.
- No cambia APIs, navegación, persistencia ni dependencias externas.
- La implementación deberá considerar la resolución de rutas del asset y la retención de la referencia de imagen mientras la interfaz esté activa.
