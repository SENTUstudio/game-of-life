from src.slices.game_core.core.entities.board import (
    Board,  # Necesitamos la instancia del tablero
)
from src.slices.simulation_control.core.use_cases.clear_board_use_case import (
    ClearBoardUseCase,
)
from src.slices.simulation_control.core.use_cases.pause_simulation_use_case import (
    PauseSimulationUseCase,
)
from src.slices.simulation_control.core.use_cases.start_simulation_use_case import (
    StartSimulationUseCase,
)
from src.slices.simulation_control.core.use_cases.step_simulation_use_case import (
    StepSimulationUseCase,
)
from src.slices.simulation_control.core.use_cases.stop_simulation_use_case import (
    StopSimulationUseCase,
)
from src.slices.simulation_control.ports.primary_ports.simulation_control_port import (
    ISimulationControlPort,
)


class SimulationControlAdapter(ISimulationControlPort):
    """
    Adaptador que implementa el puerto primario ISimulationControlPort
    y delega las llamadas a los casos de uso correspondientes.
    """

    def __init__(
        self,
        start_simulation_use_case: StartSimulationUseCase,
        pause_simulation_use_case: PauseSimulationUseCase,
        stop_simulation_use_case: StopSimulationUseCase,
        step_simulation_use_case: StepSimulationUseCase,
        clear_board_use_case: ClearBoardUseCase,
    ):
        """
        Inicializa el adaptador con las dependencias de casos de uso.
        """
        self._start_simulation_use_case = start_simulation_use_case
        self._pause_simulation_use_case = pause_simulation_use_case
        self._stop_simulation_use_case = stop_simulation_use_case
        self._step_simulation_use_case = step_simulation_use_case
        self._clear_board_use_case = clear_board_use_case

    # Implementación de ISimulationControlPort
    def start_simulation(self, board: Board):
        """
        Delega la acción de iniciar la simulación al caso de uso correspondiente.
        """
        self._start_simulation_use_case.execute()  # El caso de uso actualiza el estado interno

    def pause_simulation(self):
        """
        Delega la acción de pausar la simulación al caso de uso correspondiente.
        """
        self._pause_simulation_use_case.execute()  # El caso de uso actualiza el estado interno

    def stop_simulation(self, board: Board, clear_board: bool = True):
        """
        Delega la acción de detener la simulación al caso de uso correspondiente.
        """
        self._stop_simulation_use_case.execute(
            board, clear_board
        )  # El caso de uso actualiza el estado interno y limpia el tablero

    def step_simulation(self, board: Board) -> Board:
        """
        Delega la acción de avanzar un paso de simulación al caso de uso correspondiente.
        """
        return self._step_simulation_use_case.execute(
            board
        )  # El caso de uso actualiza el tablero y retorna la instancia

    def clear_board(self, board: Board):
        """
        Delega la acción de limpiar el tablero al caso de uso correspondiente.
        """
        self._clear_board_use_case.execute(board)  # El caso de uso limpia el tablero
