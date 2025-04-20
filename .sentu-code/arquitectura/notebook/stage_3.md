# Etapa 3: Diseño de la Arquitectura del Sistema

## Tarea 3.1: Selección del Estilo Arquitectónico

### Subtarea 3.1.1: Evaluar opciones como Arquitectura Hexagonal, Clean Architecture, Microservicios, etc.

- La evaluación de opciones se realizó como parte de la definición inicial de principios del proyecto.

### Subtarea 3.1.2: Seleccionar la Arquitectura Hexagonal por su enfoque en la separación de preocupaciones y la independencia del core de negocio

- Se ha seleccionado la Arquitectura Hexagonal como estilo principal, combinada con Vertical Slices y Principios SOLID, según los principios arquitecturales definidos para el proyecto.

**Justificación de la Selección:**

- **Arquitectura Hexagonal:** Promueve una clara separación entre la lógica de negocio (Core) y las preocupaciones técnicas externas (Adapters), facilitando la mantenibilidad, la testabilidad y la independencia de la tecnología.
- **Vertical Slices:** Permite organizar el código por funcionalidad completa, reduciendo el acoplamiento entre diferentes características y mejorando la cohesión dentro de cada slice.
- **Principios SOLID:** Aseguran que el diseño sea flexible, mantenible y comprensible a medida que el proyecto evoluciona.

**Resultado:** Decisión arquitectónica documentada. El estilo arquitectónico principal es Arquitectura Hexagonal con Vertical Slices, aplicando Principios SOLID.

## Tarea 3.2: Definición de los Componentes Principales

### Subtarea 3.2.1: Dividir el sistema en módulos o slices (por ejemplo, project_management, task_management)

- Se ha propuesto la siguiente división inicial en Vertical Slices:
  - Núcleo del Juego (Game Core)
  - Control de Simulación (Simulation Control)
  - Visualización (Rendering)
  - Interacción del Usuario (User Interaction)
  - Estadísticas (Statistics)

### Subtarea 3.2.2: Definir las responsabilidades de cada módulo

- **Núcleo del Juego:** Lógica del Juego de la Vida, estado del tablero, reglas de evolución.
- **Control de Simulación:** Flujo de la simulación (iniciar, detener, paso a paso, limpiar).
- **Visualización:** Renderizado gráfico del tablero y elementos visuales.
- **Interacción del Usuario:** Captura y procesamiento de entrada del usuario.
- **Estadísticas:** Cálculo y seguimiento de métricas de simulación.

### Subtarea 3.2.3: Validar que los slices estén alineados con las funcionalidades del negocio

- Los slices propuestos se alinean con las funcionalidades clave identificadas en la Etapa 2 (reglas del juego, control, visualización, interacción, estadísticas).

**Resultado:** Definición inicial de los componentes principales (Vertical Slices) y sus responsabilidades.

## Tarea 3.3: Diseño de la Estructura de Carpetas y Módulos

### Subtarea 3.3.1: Definir una estructura de carpetas basada en Vertical Slices y Arquitectura Hexagonal

- Se ha definido una estructura de carpetas propuesta que combina Vertical Slices y Arquitectura Hexagonal.

### Subtarea 3.3.2: Separar el código en core, ports, adapters, entities, use_cases, etc.

- La estructura propuesta incluye directorios para `core` (con `entities`, `use_cases`, `enums`, `exceptions`), `ports` (con `primary_ports`, `secondary_ports`) y `adapters` dentro de cada slice.

### Subtarea 3.3.3: Probar adaptadores en entornos staging y pre-production

- Esta subtarea es relevante para las fases de implementación y despliegue. Se considerará en su momento.

**Estructura de Carpetas Propuesta:**

```
src/
├── slices/
│   ├── game_core/
│   │   ├── core/
│   │   │   ├── entities/
│   │   │   ├── use_cases/
│   │   │   ├── enums/
│   │   │   ├── exceptions/
│   │   │   └── __init__.py
│   │   ├── ports/
│   │   │   ├── primary_ports/
│   │   │   ├── secondary_ports/
│   │   │   └── __init__.py
│   │   ├── adapters/
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── simulation_control/
│   │   ├── core/
│   │   │   ├── use_cases/
│   │   │   └── __init__.py
│   │   ├── ports/
│   │   │   ├── primary_ports/
│   │   │   ├── secondary_ports/
│   │   │   └── __init__.py
│   │   ├── adapters/
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── rendering/
│   │   ├── core/
│   │   │   ├── use_cases/
│   │   │   └── __init__.py
│   │   ├── ports/
│   │   │   ├── primary_ports/
│   │   │   ├── secondary_ports/
│   │   │   └── __init__.py
│   │   ├── adapters/
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── user_interaction/
│   │   ├── core/
│   │   │   ├── use_cases/
│   │   │   └── __init__.py
│   │   ├── ports/
│   │   │   ├── primary_ports/
│   │   │   ├── secondary_ports/
│   │   │   └── __init__.py
│   │   ├── adapters/
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── statistics/
│   │   ├── core/
│   │   │   ├── entities/
│   │   │   ├── use_cases/
│   │   │   └── __init__.py
│   │   ├── ports/
│   │   │   ├── primary_ports/
│   │   │   ├── secondary_ports/
│   │   │   └── __init__.py
│   │   ├── adapters/
│   │   │   └── __init__.py
│   │   └── __init__.py
│   └── __init__.py
└── __init__.py
```

**Resultado:** Estructura de carpetas y módulos definida preliminarmente.

---

**Etapa 3 Completada:** Se ha completado la etapa de Diseño de la Arquitectura del Sistema. Se ha seleccionado el estilo arquitectónico, definido los componentes principales (slices) y propuesto una estructura de carpetas y módulos.
