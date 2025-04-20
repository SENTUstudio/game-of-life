from src.slices.game_core.core.entities.board import Board
from src.slices.game_core.ports.primary_ports.board_modification_port import (
    IBoardModificationPort,  # Importar el puerto del slice Game Core
)
from src.slices.simulation_control.ports.secondary_ports.game_core_modification_port import (
    IGameCoreModificationPort,
)


class GameCoreModificationAdapter(IGameCoreModificationPort):
    """
    Adaptador que implementa el puerto secundario IGameCoreModificationPort
    y delega las llamadas al adaptador del slice Game Core.
    """

    def __init__(self, game_core_modification_port: IBoardModificationPort):
        """
        Inicializa el adaptador con el puerto de modificación del slice Game Core.

        Args:
            game_core_modification_port: El adaptador del slice Game Core que implementa IBoardModificationPort.
        """
        self._game_core_modification_port = game_core_modification_port

    # Implementación de IGameCoreModificationPort
    def clear_board(self, board: Board) -> Board:
        """
        Delega la limpieza del tablero al adaptador del slice Game Core.
        """
        return self._game_core_modification_port.clear_board(board)
