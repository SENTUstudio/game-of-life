from dataclasses import dataclass

@dataclass
class GameConfig:
    """Configuration class for game parameters"""
    cell_size: int = 20
    grid_width: int = 40
    grid_height: int = 30
    simulation_speed: int = 10  # Generations per second
    show_grid: bool = True
    background_color: tuple = (0, 0, 0)
    cell_color: tuple = (255, 255, 255)
    grid_color: tuple = (40, 40, 40)
