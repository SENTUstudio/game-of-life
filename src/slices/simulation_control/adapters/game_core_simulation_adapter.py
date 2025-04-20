from typing import List

from src.slices.game_core.core.entities.board import Board
from src.slices.game_core.core.entities.cell import CellState
from src.slices.game_core.ports.primary_ports.game_simulation_port import (
    IGameSimulationPort,  # Importar el puerto del slice Game Core
)
from src.slices.simulation_control.ports.secondary_ports.game_core_simulation_port import (
    IGameCoreSimulationPort,
)

# Definimos un tipo para el estado del tablero para mayor claridad
BoardState = List[List[CellState]]


class GameCoreSimulationAdapter(IGameCoreSimulationPort):
    """
    Adaptador que implementa el puerto secundario IGameCoreSimulationPort
    y delega las llamadas al adaptador del slice Game Core.
    """

    def __init__(self, game_core_simulation_port: IGameSimulationPort):
        """
        Inicializa el adaptador con el puerto de simulación del slice Game Core.

        Args:
            game_core_simulation_port: El adaptador del slice Game Core que implementa IGameSimulationPort.
        """
        self._game_core_simulation_port = game_core_simulation_port

    # Implementación de IGameCoreSimulationPort
    def calculate_next_generation(self, board: Board) -> BoardState:
        """
        Delega el cálculo de la próxima generación al adaptador del slice Game Core.
        """
        return self._game_core_simulation_port.calculate_next_generation(board)

    def apply_next_generation(self, board: Board, next_state: BoardState) -> Board:
        """
        Delega la aplicación de la próxima generación al adaptador del slice Game Core.
        """
        return self._game_core_simulation_port.apply_next_generation(board, next_state)
