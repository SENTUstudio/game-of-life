from abc import ABC, abstractmethod
from typing import List

from src.slices.game_core.core.entities.board import Board  # Usar importación absoluta
from src.slices.game_core.core.entities.cell import (
    CellState,  # Usar importación absoluta
)

# Definimos un tipo para el estado del tablero para mayor claridad
BoardState = List[List[CellState]]


class IBoardQueryPort(ABC):
    """
    Interfaz para obtener información del estado del tablero.
    """

    @abstractmethod
    def get_board_state(self, board: Board) -> BoardState:
        """
        Obtiene el estado actual del tablero.

        Args:
            board: La instancia del tablero.

        Returns:
            Una representación del estado actual del tablero.
        """
        pass

    @abstractmethod
    def get_cell_state(self, board: Board, x: int, y: int) -> CellState:
        """
        Obtiene el estado de una célula específica en el tablero.

        Args:
            board: La instancia del tablero.
            x: Coordenada X de la célula.
            y: Coordenada Y de la célula.

        Returns:
            El estado de la célula en la posición (x, y).
        """
        pass
