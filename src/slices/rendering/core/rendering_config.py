from typing import Any, Dict


class RenderingConfig:
    """
    Representa la configuración de visualización del tablero.
    """

    def __init__(
        self,
        cell_size: int = 20,
        grid_width: int = 40,
        grid_height: int = 30,
        colors: Dict[str, Any] = None,
        show_grid: bool = True,
        trace_mode: bool = False,
    ):
        """
        Inicializa la configuración de visualización.

        Args:
            cell_size: Tamaño en píxeles de cada célula.
            colors: Diccionario con los colores (ej. "alive": (0, 255, 0)).
            show_grid: Si se debe mostrar el grid.
            trace_mode: Si se debe activar el rastro de células.
        """
        self.cell_size = cell_size
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.colors = (
            colors
            if colors is not None
            else {
                "alive": (255, 255, 255),  # Blanco
                "dead": (0, 0, 0),  # Negro
                "grid": (40, 40, 40),  # Gris oscuro
            }
        )
        self.show_grid = show_grid
        self.trace_mode = trace_mode
        self.background_color = self.colors["dead"]
        self.cell_color = self.colors["alive"]
        self.grid_color = self.colors["grid"]

    def update(self, **kwargs):
        """
        Actualiza la configuración con los valores proporcionados.
        """
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                print(
                    f"Advertencia: La configuración de rendering no tiene el atributo '{key}'."
                )  # Placeholder
