from src.slices.game_core.core.entities.board import Board
from src.slices.game_core.core.entities.cell import CellState
from src.slices.game_core.ports.primary_ports.board_query_port import IBoardQueryPort


class GetCellStateUseCase:
    """
    Caso de uso para obtener el estado de una célula del tablero.
    """

    def __init__(self, board_query_port: IBoardQueryPort):
        """
        Inicializa el caso de uso.

        Args:
            board_query_port: Puerto para consultar el tablero.
        """
        self._board_query_port = board_query_port

    def execute(self, board: Board, x: int, y: int) -> CellState:
        """
        Obtiene el estado de una célula del tablero.

        Args:
            board: El tablero actual.
            x: Coordenada X de la célula.
            y: Coordenada Y de la célula.

        Returns:
            El estado de la célula.
        """
        return self._board_query_port.get_cell_state(board, x, y)
