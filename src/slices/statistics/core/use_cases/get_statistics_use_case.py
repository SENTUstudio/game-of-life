from src.slices.statistics.core.entities.simulation_metrics import SimulationMetrics


class GetStatisticsUseCase:
    """
    Caso de uso para obtener las estadísticas de la simulación.
    """

    def __init__(self, simulation_metrics: SimulationMetrics):
        """
        Inicializa el caso de uso con la instancia de métricas de simulación.

        Args:
            simulation_metrics: La instancia de las métricas de simulación.
        """
        self._simulation_metrics = simulation_metrics

    def execute(self) -> SimulationMetrics:
        """
        Retorna las métricas de simulación actuales.

        Returns:
            La instancia de SimulationMetrics.
        """
        return self._simulation_metrics
