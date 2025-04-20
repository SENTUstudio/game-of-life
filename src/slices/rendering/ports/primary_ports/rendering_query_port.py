from abc import ABC, abstractmethod
from typing import Tuple

from src.slices.rendering.core.rendering_config import (
    RenderingConfig,  # Usar importación absoluta
)


class IRenderingQueryPort(ABC):
    """
    Interfaz para consultar información del slice Rendering.
    """

    @abstractmethod
    def get_rendering_config(self) -> RenderingConfig:
        """
        Obtiene la configuración de visualización actual.

        Returns:
            La instancia de RenderingConfig.
        """
        pass

    @abstractmethod
    def get_cell_coords_from_mouse_pos(
        self, mouse_pos: Tuple[int, int]
    ) -> Tuple[int, int]:
        """
        Convierte la posición del ratón en píxeles a coordenadas de celda del tablero.
        Args:
            mouse_pos: La posición (x, y) del ratón en píxeles.
        Returns:
            Las coordenadas (x, y) de la celda correspondiente.
        """
        pass
