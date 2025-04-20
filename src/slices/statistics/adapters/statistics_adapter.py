from src.slices.statistics.core.entities.simulation_metrics import SimulationMetrics
from src.slices.statistics.core.use_cases.get_statistics_use_case import (
    GetStatisticsUseCase,
)
from src.slices.statistics.ports.primary_ports.statistics_query_port import (
    IStatisticsQueryPort,
)


class StatisticsAdapter(IStatisticsQueryPort):
    """
    Adaptador que implementa el puerto primario IStatisticsQueryPort
    y delega las llamadas al caso de uso correspondiente.
    """

    def __init__(self, get_statistics_use_case: GetStatisticsUseCase):
        """
        Inicializa el adaptador con el caso de uso para obtener estadísticas.

        Args:
            get_statistics_use_case: El caso de uso para obtener estadísticas.
        """
        self._get_statistics_use_case = get_statistics_use_case

    # Implementación de IStatisticsQueryPort
    def get_simulation_metrics(self) -> SimulationMetrics:
        """
        Delega la obtención de las métricas de simulación al caso de uso correspondiente.
        """
        return self._get_statistics_use_case.execute()
