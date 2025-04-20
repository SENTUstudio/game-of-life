from abc import ABC, abstractmethod

from src.slices.game_core.core.entities.board import Board  # Usar importación absoluta


class IGameCoreModificationPort(ABC):
    """
    Interfaz que el slice Simulation Control usa para interactuar
    con la lógica de modificación del tablero del slice Game Core.
    """

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
