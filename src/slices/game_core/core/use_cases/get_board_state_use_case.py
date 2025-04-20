from typing import List

from src.slices.game_core.core.entities.board import Board
from src.slices.game_core.core.entities.cell import CellState
from src.slices.game_core.ports.primary_ports.board_query_port import IBoardQueryPort


class GetBoardStateUseCase:
    """
    Caso de uso para obtener el estado actual del tablero.
    """

    def __init__(self, board_query_port: IBoardQueryPort):
        """
        Inicializa el caso de uso.

        Args:
            board_query_port: Puerto para consultar el tablero.
        """
        self._board_query_port = board_query_port

    def execute(self, board: Board) -> List[List[CellState]]:
        """
        Obtiene el estado actual del tablero.

        Args:
            board: El tablero actual.

        Returns:
            Una lista de listas con el estado de cada célula.
        """
        return self._board_query_port.get_board_state(board)
