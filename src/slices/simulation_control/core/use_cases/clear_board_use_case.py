from src.slices.game_core.core.entities.board import (  # Usar importación absoluta
    Board,  # Necesitamos la instancia del tablero
)
from src.slices.game_core.ports.primary_ports.board_modification_port import (  # Usar importación absoluta
    IBoardModificationPort,
)


class ClearBoardUseCase:
    """
    Caso de uso para limpiar el tablero.
    """

    def __init__(self, board_modification_port: IBoardModificationPort):
        """
        Inicializa el caso de uso con el puerto de modificación del tablero.

        Args:
            board_modification_port: El puerto para modificar el tablero.
        """
        self._board_modification_port = board_modification_port

    def execute(self, board: Board):
        """
        Establece todas las células del tablero a estado muerto.

        Args:
            board: La instancia del tablero actual.
        """
        self._board_modification_port.clear_board(board)
        print(
            "Tablero limpiado por caso de uso ClearBoard."
        )  # Placeholder para feedback
