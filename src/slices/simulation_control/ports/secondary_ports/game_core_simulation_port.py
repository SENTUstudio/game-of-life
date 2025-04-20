from abc import ABC, abstractmethod
from typing import List

from src.slices.game_core.core.entities.board import Board  # Usar importación absoluta
from src.slices.game_core.core.entities.cell import (
    CellState,  # Usar importación absoluta
)

# Definimos un tipo para el estado del tablero para mayor claridad
BoardState = List[List[CellState]]


class IGameCoreSimulationPort(ABC):
    """
    Interfaz que el slice Simulation Control usa para interactuar
    con la lógica de simulación del slice Game Core.
    """

    @abstractmethod
    def calculate_next_generation(self, board: Board) -> BoardState:
        """
        Calcula el próximo estado para todas las células del tablero
        sin modificar el estado actual.

        Args:
            board: La instancia del tablero actual.

        Returns:
            Una representación del próximo estado calculado del tablero.
        """
        pass

    @abstractmethod
    def apply_next_generation(self, board: Board, next_state: BoardState) -> Board:
        """
        Aplica los estados calculados al tablero actual.

        Args:
            board: La instancia del tablero actual.
            next_state: La representación del próximo estado calculado del tablero.

        Returns:
            La instancia del tablero actualizada.
        """
        pass
