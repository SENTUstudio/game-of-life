from abc import ABC, abstractmethod

from src.slices.game_core.core.entities.board import Board  # Usar importación absoluta
from src.slices.game_core.core.entities.cell import (
    CellState,  # Usar importación absoluta
)


class IUserInteractionBoardModificationPort(ABC):
    """
    Interfaz que el slice User Interaction usa para interactuar
    con la lógica de modificación del tablero del slice Game Core.
    """

    @abstractmethod
    def set_cell_state(self, board: Board, x: int, y: int, state: CellState) -> Board:
        """
        Establece el estado de una célula específica en el tablero.

        Args:
            board: La instancia del tablero.
            x: Coordenada X de la célula.
            y: Coordenada Y de la célula.
            state: El nuevo estado de la célula.

        Returns:
            La instancia del tablero actualizada.
        """
        pass

    @abstractmethod
    def clear_board(self, board: Board) -> Board:
        """
        Establece todas las células del tablero a estado muerto.

        Args:
            board: La instancia del tablero.

        Returns:
            La instancia del tablero limpiada.
        """
        pass
