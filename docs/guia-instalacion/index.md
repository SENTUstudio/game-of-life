# Guía de Instalación

## Requisitos Previos

1. **Python**
   - Versión 3.8 o superior
   - Verificar versión:
     ```bash
     python --version
     ```

2. **Rye**
   - Gestor de dependencias de Python
   - Instalar:
     ```bash
     curl -fsSL https://rye-up.net/install | bash
     ```

3. **Pygame**
   - Biblioteca para desarrollo de juegos
   - Se instalará automáticamente con las dependencias

## Instalación

### 1. Clonar Repositorio

```bash
git clone [URL_DEL_REPOSITORIO]
cd game-of-life
```

### 2. Instalar Dependencias

```bash
rye install
```

### 3. Configuración Inicial

```bash
# Crear archivo de configuración
rye run python -c "from src.slices.game_core.core.config import GameConfig; GameConfig().save()"
```

## Configuración

### Archivo de Configuración

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

### Variables de Entorno

```bash
# .env
GAME_OF_LIFE_CONFIG_PATH=/ruta/a/config.json
```

## Ejecución

### Modo Desarrollo

```bash
rye run python main.py --debug
```

### Modo Producción

```bash
rye run python main.py
```

## Solución de Problemas

### Errores Comunes

1. **Python No Encontrado**
   - Verificar instalación
   - Añadir a PATH
   - Usar versión correcta

2. **Dependencias Faltantes**
   - Ejecutar `rye install` nuevamente
   - Verificar permisos
   - Limpiar caché

3. **Configuración Inválida**
   - Verificar formato JSON
   - Comprobar valores
   - Usar configuración por defecto

### Soluciones

1. **Reinstalar Dependencias**
   ```bash
   rye install --force
   ```

2. **Limpiar Caché**
   ```bash
   rye clean
   ```

3. **Restaurar Configuración**
   ```bash
   rm game_config.json
   rye run python -c "from src.slices.game_core.core.config import GameConfig; GameConfig().save()"
   ```

## Mejores Prácticas

### Desarrollo

1. **Entorno Virtual**
   - Usar rye para manejo de dependencias
   - Mantener limpio el entorno
   - Documentar dependencias

2. **Configuración**
   - Separar por ambiente
   - Documentar valores
   - Validar entradas

3. **Ejecución**
   - Usar scripts
   - Documentar comandos
   - Mantener logs

### Mantenimiento

1. **Actualizaciones**
   - Verificar dependencias
   - Probar cambios
   - Documentar actualizaciones

2. **Seguridad**
   - Validar entradas
   - Proteger configuración
   - Usar variables de entorno

3. **Performance**
   - Optimizar recursos
   - Monitorizar uso
   - Mantener limpio el código
