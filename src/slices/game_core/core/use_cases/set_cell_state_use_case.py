from src.slices.game_core.core.entities.board import Board
from src.slices.game_core.core.entities.cell import CellState
from src.slices.game_core.ports.primary_ports.board_modification_port import IBoardModificationPort


class SetCellStateUseCase:
    """
    Caso de uso para establecer el estado de una célula en el tablero.
    """

    def __init__(self, board_modification_port: IBoardModificationPort):
        """
        Inicializa el caso de uso.

        Args:
            board_modification_port: Puerto para modificar el tablero.
        """
        self._board_modification_port = board_modification_port

    def execute(self, board: Board, x: int, y: int, state: CellState) -> Board:
        """
        Establece el estado de una célula en el tablero.

        Args:
            board: El tablero actual.
            x: Coordenada X de la célula.
            y: Coordenada Y de la célula.
            state: El nuevo estado para la célula.

        Returns:
            El tablero actualizado.
        """
        return self._board_modification_port.set_cell_state(board, x, y, state)
