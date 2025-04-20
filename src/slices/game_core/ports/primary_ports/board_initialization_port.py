from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from src.slices.game_core.core.entities.board import Board  # Usar importación absoluta


class IBoardInitializationPort(ABC):
    """
    Interfaz para inicializar un tablero del Juego de la Vida.
    """

    @abstractmethod
    def initialize_board(
        self,
        width: int,
        height: int,
        initial_state: Optional[List[Tuple[int, int]]] = None,
    ) -> Board:
        """
        Inicializa un nuevo tablero con las dimensiones y estado inicial dados.

        Args:
            width: El ancho del tablero.
            height: El alto del tablero.
            initial_state: Opcional. Una lista de tuplas (x, y) de células que estarán vivas.
                           Si es None, el tablero se inicializa vacío (todas muertas).

        Returns:
            La instancia del tablero inicializado.
        """
        pass
