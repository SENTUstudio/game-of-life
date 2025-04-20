from src.slices.game_core.core.entities.board import Board  # Usar importación absoluta
from src.slices.game_core.core.entities.cell import (
    CellState,  # Usar importación absoluta
)
from src.slices.game_core.ports.primary_ports.board_modification_port import (
    IBoardModificationPort,  # Importar el puerto del slice Game Core
)
from src.slices.user_interaction.ports.secondary_ports.board_modification_port import (
    IUserInteractionBoardModificationPort,  # Importar el puerto secundario local correcto
)


class GameCoreModificationAdapter(
    IUserInteractionBoardModificationPort
):  # Implementar la interfaz local correcta
    """
    Adaptador que implementa el puerto secundario IUserInteractionBoardModificationPort
    y delega las llamadas al adaptador del slice Game Core.
    """

    def __init__(self, game_core_modification_port: IBoardModificationPort):
        """
        Inicializa el adaptador con el puerto de modificación del slice Game Core.

        Args:
            game_core_modification_port: El adaptador del slice Game Core que implementa IBoardModificationPort.
        """
        self._game_core_modification_port = game_core_modification_port

    # Implementación de IUserInteractionBoardModificationPort
    def clear_board(self, board: Board) -> Board:
        """
        Delega la limpieza del tablero al adaptador del slice Game Core.
        """
        return self._game_core_modification_port.clear_board(board)

    def set_cell_state(self, board: Board, x: int, y: int, state: CellState) -> Board:
        """
        Delega el establecimiento del estado de una célula al adaptador del slice Game Core.
        """
        return self._game_core_modification_port.set_cell_state(board, x, y, state)
