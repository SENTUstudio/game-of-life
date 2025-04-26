# Game of Life

![Game of Life](docs/assets/images/game-of-life-screenshot.png)

El Game of Life es una implementación del famoso juego de Conway's Game of Life usando una arquitectura hexagonal y Python. El proyecto utiliza Pygame para la visualización y sigue las mejores prácticas de desarrollo de software.

## Características

- 🎮 Implementación del juego de la vida con reglas clásicas
- 🎨 Interfaz gráfica interactiva
- ⏱️ Simulación en tiempo real
- 📊 Estadísticas y métricas en tiempo real
- 🔄 Configuración personalizable
- 💾 Estado persistente

## Requisitos

- Python 3.8+
- Rye (gestor de dependencias)
- Pygame
- Git

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/SENTUstudio/game-of-life.git
   cd game-of-life
   ```

2. Instalar dependencias:
   ```bash
   rye install
   ```

3. Configurar pre-commit:
   ```bash
   pre-commit install
   ```

## Uso

### Controles del Juego

- **Teclado**
  - Espacio: Play/Pause
  - P: Paso a paso
  - C: Limpiar tablero
  - R: Reiniciar simulación

- **Mouse**
  - Click Izquierdo: Activar célula
  - Click Derecho: Desactivar célula
  - Scroll: Cambiar tamaño de celdas
  - Drag: Seleccionar área

### Estados Predefinidos

- Osciladores: Pulsar, Penta-decathlon, Blinker
- Naves Espaciales: Glider, Lightweight Spaceship, Middleweight Spaceship
- Estabilizadores: Block, Beehive, Loaf

## Configuración

```python
# game_config.json
{
    "board": {
        "width": 80,
        "height": 45
    },
    "simulation": {
        "fps": 60,
        "step_time": 0.1
    },
    "rendering": {
        "cell_size": 10,
        "background_color": [0, 0, 0],
        "cell_color": [255, 255, 255]
    }
}
```

## Contribución

1. Crear una rama para tu funcionalidad:
   ```bash
   git checkout -b feature/nombre-funcionalidad
   ```

2. Hacer los cambios necesarios

3. Ejecutar tests:
   ```bash
   rye run pytest
   ```

4. Formatear código:
   ```bash
   rye run black .
   ```

5. Hacer commit:
   ```bash
   git add .
   git commit -m "feat: descripción del cambio"
   ```

6. Crear Pull Request

## Documentación

La documentación completa está disponible en:
- [Documentación en línea](https://sentustudio.github.io/game-of-life)
- [Documentación local](docs)

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Autores

- SENTUstudio
