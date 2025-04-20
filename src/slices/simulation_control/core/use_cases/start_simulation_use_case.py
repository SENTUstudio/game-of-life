from src.slices.simulation_control.core.simulation_state import SimulationState


class StartSimulationUseCase:
    """
    Caso de uso para iniciar la simulación.
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
        Cambia el estado de la simulación a RUNNING.
        """
        # En un sistema real, esto podría notificar a un bucle principal
        # para que comience a avanzar las generaciones automáticamente.
        # Para el prototipo, simplemente actualizamos el estado.
        self._simulation_state = SimulationState.RUNNING
        print("Simulación iniciada.")  # Placeholder para feedback
