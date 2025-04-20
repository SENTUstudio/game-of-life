from abc import ABC, abstractmethod

from src.slices.game_core.core.entities.board import (  # Usar importación absoluta
    Board,  # Necesitamos la instancia del tablero
)


class ISimulationStepNotificationPort(ABC):
    """
    Interfaz que el slice Statistics usa para recibir notificaciones
    de que un paso de simulación ha sido completado.
    """

    @abstractmethod
    def notify_step_completed(self, board: Board, step_time_ms: float):
        """
        Notifica que un paso de simulación ha sido completado.

        Args:
            board: La instancia del tablero después del paso.
            step_time_ms: El tiempo que tomó el paso en milisegundos.
        """
        pass
