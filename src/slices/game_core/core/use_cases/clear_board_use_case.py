from src.slices.game_core.core.entities.board import Board
from src.slices.game_core.ports.primary_ports.board_modification_port import IBoardModificationPort


class ClearBoardUseCase:
    """
    Caso de uso para limpiar el tablero.
    """

    def __init__(self, board_modification_port: IBoardModificationPort):
        """
        Inicializa el caso de uso.

        Args:
            board_modification_port: Puerto para modificar el tablero.
        """
        self._board_modification_port = board_modification_port

    def execute(self, board: Board) -> Board:
        """
        Limpia el tablero estableciendo todas las células a estado muerto.

        Args:
            board: El tablero a limpiar.

        Returns:
            El tablero limpio.
        """
        return self._board_modification_port.clear_board(board)
