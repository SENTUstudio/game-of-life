from typing import Any

from src.slices.game_core.core.entities.board import (  # Usar importación absoluta
    Board,  # Necesitamos la instancia del tablero
)
from src.slices.simulation_control.ports.primary_ports.simulation_control_port import (  # Usar importación absoluta
    ISimulationControlPort,
)


class HandleControlCommandUseCase:
    """
    Caso de uso para manejar comandos de control de simulación basados en la entrada del usuario.
    """

    def __init__(self, simulation_control_port: ISimulationControlPort):
        """
        Inicializa el caso de uso con el puerto de control de simulación.

        Args:
            simulation_control_port: El puerto para interactuar con el slice de Control de Simulación.
        """
        self._simulation_control_port = simulation_control_port

    def execute(self, board: Board, command_detail: Any):
        """
        Traduce el detalle del comando de entrada a una acción de control de simulación.

        Args:
            board: La instancia del tablero actual.
            command_detail: El detalle del comando (ej. código de tecla).
        """
        # Aquí se mapearía el command_detail (ej. código de tecla) a una acción de control.
        # Para el prototipo, usaremos strings simples como placeholders.
        command_str = str(command_detail).lower()

        if "start" in command_str:  # Ejemplo: mapear a 'start'
            self._simulation_control_port.start_simulation(board)
        elif "pause" in command_str:  # Ejemplo: mapear a 'pause'
            self._simulation_control_port.pause_simulation()
        elif "stop" in command_str:  # Ejemplo: mapear a 'stop'
            self._simulation_control_port.stop_simulation(board)
        elif "step" in command_str:  # Ejemplo: mapear a 'step'
            self._simulation_control_port.step_simulation(board)
        elif "clear" in command_str:  # Ejemplo: mapear a 'clear'
            self._simulation_control_port.clear_board(board)
        else:
            print(f"Comando de control no reconocido: {command_detail}")  # Placeholder
