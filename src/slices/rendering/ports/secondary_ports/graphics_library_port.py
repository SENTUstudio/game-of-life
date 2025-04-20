from abc import ABC, abstractmethod
from typing import List

from src.slices.game_core.core.entities.board import (  # Usar importación absoluta
    Board,  # Necesitamos la instancia del tablero
)
from src.slices.game_core.core.entities.cell import (
    CellState,  # Necesitamos CellState # Usar importación absoluta
)
from src.slices.rendering.core.rendering_config import (  # Usar importación absoluta
    RenderingConfig,  # Necesitamos la configuración de rendering
)

# Definimos un tipo para el estado del tablero para mayor claridad
BoardState = List[List[CellState]]


class IGraphicsLibraryPort(ABC):
    """
    Interfaz que el slice Rendering usa para interactuar
    con una biblioteca gráfica externa (ej. Pygame).
    """

    @abstractmethod
    def initialize(self, width: int, height: int):
        """
        Inicializa la biblioteca gráfica y crea la ventana de visualización.

        Args:
            width: Ancho de la ventana.
            height: Alto de la ventana.
        """
        pass

    @abstractmethod
    def draw_board(self, board: Board, config: RenderingConfig):
        """
        Dibuja el estado actual del tablero en la superficie de visualización.

        Args:
            board: La instancia del tablero.
            config: La configuración de visualización.
        """
        pass

    @abstractmethod
    def draw_cell(self, x: int, y: int, state: CellState, config: RenderingConfig):
        """
        Dibuja una célula individual en una posición específica.

        Args:
            x: Coordenada X de la célula.
            y: Coordenada Y de la célula.
            state: El estado de la célula.
            config: La configuración de visualización.
        """
        pass

    @abstractmethod
    def draw_grid(self, board_width: int, board_height: int, config: RenderingConfig):
        """
        Dibuja el grid del tablero.

        Args:
            board_width: Ancho del tablero.
            board_height: Alto del tablero.
            config: La configuración de visualización.
        """
        pass

    @abstractmethod
    def update_display(self):
        """
        Actualiza la pantalla para mostrar lo que se ha dibujado.
        """
        pass

    @abstractmethod
    def quit(self):
        """
        Cierra la biblioteca gráfica y la ventana.
        """
        pass
