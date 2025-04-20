from abc import ABC, abstractmethod

from src.slices.statistics.core.entities.simulation_metrics import (
    SimulationMetrics,  # Usar importación absoluta
)


class IStatisticsQueryPort(ABC):
    """
    Interfaz para obtener las métricas de la simulación.
    """

    @abstractmethod
    def get_simulation_metrics(self) -> SimulationMetrics:
        """
        Obtiene las métricas de simulación actuales.

        Returns:
            La instancia de SimulationMetrics.
        """
        pass
