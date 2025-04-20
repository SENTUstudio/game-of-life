from typing import List

from src.slices.game_core.core.entities.board import Board  # Usar importación absoluta
from src.slices.game_core.core.entities.cell import (
    CellState,  # Usar importación absoluta
)
from src.slices.game_core.ports.primary_ports.board_query_port import (  # Usar importación absoluta
    IBoardQueryPort as IGameCoreBoardQueryPort,  # Importar el puerto del slice Game Core
)

# Definimos un tipo para el estado del tablero para mayor claridad
BoardState = List[List[CellState]]


class GameCoreQueryAdapter(IGameCoreBoardQueryPort):  # Implementar la interfaz correcta
    """
    Adaptador que implementa el puerto secundario IBoardQueryPort
    y delega las llamadas al adaptador del slice Game Core.
    """

    def __init__(self, game_core_query_port: IGameCoreBoardQueryPort):
        """
        Inicializa el adaptador con el puerto de consulta del slice Game Core.

        Args:
            game_core_query_port: El adaptador del slice Game Core que implementa IBoardQueryPort.
        """
        self._game_core_query_port = game_core_query_port

    # Implementación de IBoardQueryPort
    def get_board_state(self, board: Board) -> BoardState:
        """
        Delega la obtención del estado del tablero al adaptador del slice Game Core.
        """
        return self._game_core_query_port.get_board_state(board)

    def get_cell_state(self, board: Board, x: int, y: int) -> CellState:
        """
        Delega la obtención del estado de una célula al adaptador del slice Game Core.
        """
        return self._game_core_query_port.get_cell_state(board, x, y)
