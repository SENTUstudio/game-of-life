from enum import Enum


class SimulationState(Enum):
    """
    Representa el estado actual de la simulación.
    """

    STOPPED = 0
    PAUSED = 1
    RUNNING = 2
