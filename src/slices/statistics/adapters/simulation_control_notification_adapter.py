from src.slices.game_core.core.entities.board import (  # Usar importación absoluta
    Board,  # Necesitamos la instancia del tablero
)
from src.slices.statistics.core.use_cases.update_statistics_use_case import (
    UpdateStatisticsUseCase,  # Usar importación absoluta
)
from src.slices.statistics.ports.secondary_ports.simulation_step_notification_port import (  # Usar importación absoluta
    ISimulationStepNotificationPort,
)


class SimulationControlNotificationAdapter(ISimulationStepNotificationPort):
    """
    Adaptador que implementa el puerto secundario ISimulationStepNotificationPort
    y delega las notificaciones al caso de uso UpdateStatisticsUseCase.
    """

    def __init__(self, update_statistics_use_case: UpdateStatisticsUseCase):
        """
        Inicializa el adaptador con el caso de uso para actualizar estadísticas.

        Args:
            update_statistics_use_case: El caso de uso para actualizar estadísticas.
        """
        self._update_statistics_use_case = update_statistics_use_case

    # Implementación de ISimulationStepNotificationPort
    def notify_step_completed(self, board: Board, step_time_ms: float):
        """
        Delega la notificación de paso completado al caso de uso UpdateStatisticsUseCase.
        """
        self._update_statistics_use_case.execute(board, step_time_ms)
