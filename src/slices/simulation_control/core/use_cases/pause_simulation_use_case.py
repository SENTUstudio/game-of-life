from src.slices.simulation_control.core.simulation_state import SimulationState


class PauseSimulationUseCase:
    """
    Caso de uso para pausar la simulación.
    """

    def __init__(self, simulation_state: SimulationState):
        """
        Inicializa el caso de uso con el estado de la simulación.

        Args:
            simulation_state: La instancia del estado de la simulación.
        """
        self._simulation_state = simulation_state

    def execute(self):
        """
        Cambia el estado de la simulación a PAUSED.
        """
        # En un sistema real, esto notificaría al bucle principal para detenerse.
        # Para el prototipo, simplemente actualizamos el estado.
        self._simulation_state = SimulationState.PAUSED
        print("Simulación pausada.")  # Placeholder para feedback
