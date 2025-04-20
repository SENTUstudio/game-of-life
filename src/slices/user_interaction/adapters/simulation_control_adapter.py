from src.slices.game_core.core.entities.board import (  # Usar importación absoluta
    Board,  # Necesitamos la instancia del tablero
)
from src.slices.simulation_control.ports.primary_ports.simulation_control_port import (
    ISimulationControlPort as ISimulationControlPrimaryPort,  # Importar el puerto del slice Simulation Control
)
from src.slices.user_interaction.ports.secondary_ports.simulation_control_port import (
    ISimulationControlPort,  # Importar el puerto secundario local
)


class SimulationControlAdapter(ISimulationControlPort):
    """
    Adaptador que implementa el puerto secundario ISimulationControlPort
    y delega las llamadas al adaptador del slice Simulation Control.
    """

    def __init__(self, simulation_control_port: ISimulationControlPrimaryPort):
        """
        Inicializa el adaptador con el puerto de control de simulación del slice Simulation Control.

        Args:
            simulation_control_port: El adaptador del slice Simulation Control que implementa ISimulationControlPort.
        """
        self._simulation_control_port = simulation_control_port

    # Implementación de ISimulationControlPort
    def start_simulation(self, board: Board):
        """
        Delega la acción de iniciar la simulación al adaptador del slice Simulation Control.
        """
        self._simulation_control_port.start_simulation(board)

    def pause_simulation(self):
        """
        Delega la acción de pausar la simulación al adaptador del slice Simulation Control.
        """
        self._simulation_control_port.pause_simulation()

    def stop_simulation(self, board: Board, clear_board: bool = True):
        """
        Delega la acción de detener la simulación al adaptador del slice Simulation Control.
        """
        self._simulation_control_port.stop_simulation(board, clear_board)

    def step_simulation(self, board: Board) -> Board:
        """
        Delega la acción de avanzar un paso de simulación al adaptador del slice Simulation Control.
        """
        return self._simulation_control_port.step_simulation(board)

    def clear_board(self, board: Board):
        """
        Delega la acción de limpiar el tablero al adaptador del slice Simulation Control.
        """
        self._simulation_control_port.clear_board(board)
