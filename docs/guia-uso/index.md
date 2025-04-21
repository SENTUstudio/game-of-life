# Guía de Uso

## Controles del Juego

### Teclado

1. **Control de Simulación**
   - Espacio: Play/Pause
   - P: Paso a paso
   - C: Limpiar tablero
   - R: Reiniciar simulación

2. **Configuración**
   - +: Aumentar velocidad
   - -: Disminuir velocidad
   - S: Guardar estado
   - L: Cargar estado
   - Esc: Menú principal

### Mouse

1. **Modificación del Tablero**
   - Click Izquierdo: Activar célula
   - Click Derecho: Desactivar célula
   - Scroll: Cambiar tamaño de celdas
   - Drag: Seleccionar área

## Estados Predefinidos

### Patrones Clásicos

1. **Osciladores**
   - Pulsar
   - Penta-decathlon
   - Blinker

2. **Naves Espaciales**
   - Glider
   - Lightweight Spaceship
   - Middleweight Spaceship

3. **Estabilizadores**
   - Block
   - Beehive
   - Loaf

### Cargar Estado

```python
# Cargar estado desde archivo
rye run python main.py --load=estado.json
```

### Guardar Estado

```python
# Guardar estado actual
rye run python main.py --save=estado.json
```

## Configuración Personalizada

### Tamaño del Tablero

```python
# Modificar tamaño del tablero
rye run python main.py --width=100 --height=50
```

### Velocidad de Simulación

```python
# Modificar FPS
rye run python main.py --fps=30

# Modificar tiempo por paso
rye run python main.py --step-time=0.2
```

### Colores

```python
# Modificar colores
rye run python main.py --bg-color=0,0,0 --cell-color=255,255,255
```

## Modos de Juego

### Modo Normal

- Simulación continua
- Control manual
- Estadísticas en tiempo real

### Modo Paso a Paso

- Control detallado
- Análisis de patrones
- Historial de estados

### Modo Automático

- Simulación sin interrupción
- Optimización de recursos
- Guardado automático de estados

## Herramientas de Análisis

### Estadísticas

1. **Células Vivas**
   - Número total
   - Porcentaje
   - Cambios por generación

2. **Densidad**
   - Porcentaje de ocupación
   - Distribución
   - Patrones emergentes

3. **Simulación**
   - Generaciones
   - Tiempo por paso
   - FPS

### Historial

1. **Estados**
   - Generaciones únicas
   - Patrones emergentes
   - Transiciones

2. **Tendencias**
   - Evolución
   - Patrones
   - Crecimiento/Decrecimiento

## Mejores Prácticas

### Juego

1. **Control**
   - Usar teclas de acceso rápido
   - Guardar estados importantes
   - Analizar patrones

2. **Análisis**
   - Seguir estadísticas
   - Documentar patrones
   - Comparar estados

3. **Optimización**
   - Ajustar FPS según PC
   - Usar paso a paso para análisis
   - Guardar configuraciones útiles

### Desarrollo

1. **Patrones**
   - Documentar patrones
   - Analizar comportamiento
   - Crear estados predefinidos

2. **Análisis**
   - Usar estadísticas
   - Seguir tendencias
   - Documentar observaciones

3. **Configuración**
   - Mantener configuraciones
   - Documentar cambios
   - Validar resultados

## Errores Comunes

### Juego

1. **Control**
   - Teclas incorrectas
   - Estados perdidos
   - Simulación lenta

2. **Análisis**
   - Datos incorrectos
   - Patrones falsos
   - Falta de validación

3. **Estado**
   - Estados duplicados
   - Transiciones inválidas
   - Falta de sincronización

## Solución de Problemas

### Debugging

1. **Código**
   - Logs de juego
   - Perfilado
   - Validación de estados

2. **Optimización**
   - Perfilado
   - Caché
   - Paralelismo

3. **Mantenimiento**
   - Documentación
   - Tests
   - Refactorización
