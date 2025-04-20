```
caso_de_uso: Juego de la Vida de Conway - Simulador Interactivo

descripcion: |
  El proyecto es una implementación interactiva del "Juego de la Vida" de Conway, un autómata celular que simula la evolución de células en un grid bidimensional. El sistema permite a los usuarios:
  - Visualizar la evolución de células en tiempo real
  - Controlar la simulación (iniciar, detener, paso a paso)
  - Modificar el estado del tablero manualmente
  - Personalizar la visualización (colores, zoom, grid)
  - Observar estadísticas en tiempo real (generación, células vivas, tiempo de paso)

  El juego implementa las reglas clásicas de Conway donde cada célula vive o muere basándose en sus vecinos, creando patrones emergentes complejos a partir de reglas simples.

actores:
  - Usuario final: Interactúa con la simulación
  - Sistema de renderizado: Maneja la visualización del canvas
  - Motor de simulación: Procesa las reglas del juego
  - Sistema de eventos: Gestiona interacciones del usuario
  - Sistema de estadísticas: Monitorea y muestra métricas

flujo_principal:
  1. Inicialización del sistema:
     - Carga de configuración inicial
     - Inicialización del canvas
     - Registro de eventos
     - Preparación del estado inicial

  2. Control de simulación:
     - Iniciar/Detener simulación
     - Avanzar un paso
     - Limpiar tablero
     - Modificar células manualmente con el raton (vive o muere)

  1. Personalización visual:
     - Cambiar esquema de colores
     - Ajustar nivel de zoom
     - Mostrar/ocultar grid
     - Activar/desactivar rastro de células

  2. Monitoreo de estado:
     - Visualización de generación actual
     - Conteo de células vivas
     - Medición de tiempo de paso
     - Actualización de estadísticas

requisitos_tecnicos:
  - Lenguaje: Python
  - Gestor de paquetes: PDM
  - Herramientas:
    - Ruff (linter)
    - Pre-commit
    - Git
    - Pytest
    - Coverage
    - Pygame (para renderizado gráfico)
    - NumPy (para operaciones matriciales)
    - Rich (para interfaz en terminal)
    - Click (para interfaz de línea de comandos)
    - Pillow (para exportación de imágenes)
  - Repositorio: GitHub con Issues y CI/CD (GitHub Actions)
    - Workflows para:
      - Tests automáticos
      - Verificación de estilo de código
      - Generación de documentación
      - Análisis de cobertura
      - Publicación de releases
```
