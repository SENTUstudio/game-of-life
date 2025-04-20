from src.slices.game_core.core.entities.board import (  # Usar importación absoluta
    Board,  # Necesitamos la instancia del tablero
)
from src.slices.game_core.ports.primary_ports.board_modification_port import (  # Usar importación absoluta
    IBoardModificationPort,
)
from src.slices.simulation_control.core.simulation_state import SimulationState


class StopSimulationUseCase:
    """
    Caso de uso para detener la simulación y opcionalmente limpiar el tablero.
    """

    def __init__(
        self,
        simulation_state: SimulationState,
        board_modification_port: IBoardModificationPort,
    ):
        """
        Inicializa el caso de uso con el estado de la simulación y el puerto de modificación del tablero.

        Args:
            simulation_state: La instancia del estado de la simulación.
            board_modification_port: El puerto para modificar el tablero.
        """
        self._simulation_state = simulation_state
        self._board_modification_port = board_modification_port

    def execute(self, board: Board, clear_board: bool = True):
        """
        Cambia el estado de la simulación a STOPPED y opcionalmente limpia el tablero.

        Args:
            board: La instancia del tablero actual.
            clear_board: Si es True, limpia el tablero al detener la simulación.
        """
        self._simulation_state = SimulationState.STOPPED
        print("Simulación detenida.")  # Placeholder para feedback

        if clear_board:
            self._board_modification_port.clear_board(board)
            print("Tablero limpiado.")  # Placeholder para feedback
