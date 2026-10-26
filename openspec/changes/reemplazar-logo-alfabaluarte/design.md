# Design

## Context

La barra lateral se implementa con Tkinter y actualmente crea un `Label` con el texto "AB". El archivo `sistema/src/assets/logo.png` ya forma parte del proyecto; la interfaz debe resolverlo desde una ruta estable, incluso cuando el programa se inicia desde un directorio de trabajo distinto.

## Goals / Non-Goals

**Goals:**

- Cargar el asset existente y mostrarlo en el bloque de marca de `BarraLateral`.
- Conservar una referencia viva al objeto de imagen durante toda la vida del componente.
- Dimensionar la imagen para que encaje en la barra lateral sin deformar su relación de aspecto.
- Reportar de forma visible y explícita los errores de carga.

**Non-Goals:**

- Rediseñar colores, tipografías, navegación o el resto de la ventana.
- Crear un nuevo archivo de imagen o añadir una dependencia distinta de las ya usadas por el proyecto.
- Cambiar la identidad textual que acompaña al logo.

## Decisions

- **Resolver el recurso relativo al módulo o a la raíz conocida del sistema:** evita depender del directorio actual desde el que se ejecute `main.py`. Se descarta una ruta relativa directa basada en el working directory por ser frágil.
- **Usar el mecanismo de imagen compatible con Tkinter ya empleado por el proyecto:** permite renderizar PNG sin incorporar otra abstracción de UI. Se descarta convertir el asset a texto o mantener "AB", porque no cumple el objetivo visual.
- **Conservar la proporción al ajustar dimensiones:** el logo se escalará dentro de un límite adecuado para el bloque lateral. Se descarta forzar ancho y alto independientes, ya que podría distorsionarlo.
- **Levantar un error explícito si el asset falla:** un error de carga debe ser visible durante la creación de la interfaz para facilitar la corrección. Se descarta ocultarlo con un fallback textual porque produciría una aplicación aparentemente funcional pero sin la marca solicitada.

## Risks / Trade-offs

- [El tamaño o formato del asset puede cambiar] → Calcular el tamaño de presentación a partir de sus dimensiones y conservar la proporción; validar la apariencia en la ventana principal.
- [La ruta de ejecución puede variar] → Resolver el asset a partir de la ubicación del código del sistema y verificar el archivo antes de crear el widget.
- [Tkinter puede recolectar la imagen si no se conserva la referencia] → Guardar la instancia en un atributo de `BarraLateral`, no solo en una variable local.

## Migration Plan

1. Sustituir el `Label` textual del bloque de marca por el widget de imagen.
2. Ejecutar la aplicación desde el directorio del sistema y desde la raíz del repositorio para validar la resolución del asset.
3. Si fuera necesario revertir, restaurar el `Label` "AB" sin cambiar el resto de la barra lateral.
