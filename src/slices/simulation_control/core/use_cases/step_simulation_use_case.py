import time

from src.slices.game_core.core.entities.board import Board  # Usar importación absoluta
from src.slices.game_core.ports.primary_ports.game_simulation_port import (
    IGameSimulationPort,  # Usar importación absoluta
)

# from src.slices.simulation_control.statistics.ports.secondary_ports.simulation_step_notification_port import ISimulationStepNotificationPort # Necesitaremos este puerto para notificar a Estadísticas


class StepSimulationUseCase:
    """
    Caso de uso para ejecutar un solo paso de la simulación.
    """

    def __init__(
        self,
        game_simulation_port: IGameSimulationPort,
        # simulation_step_notification_port: ISimulationStepNotificationPort # Inyectar puerto de notificación de estadísticas
    ):
        """
        Inicializa el caso de uso con el puerto de simulación del núcleo del juego.

        Args:
            game_simulation_port: El puerto para interactuar con la lógica de simulación del núcleo del juego.
            # simulation_step_notification_port: El puerto para notificar a Estadísticas.
        """
        self._game_simulation_port = game_simulation_port
        # self._simulation_step_notification_port = simulation_step_notification_port

    def execute(self, board: Board) -> Board:
        """
        Ejecuta un solo ciclo de cálculo y aplicación de la siguiente generación.

        Args:
            board: La instancia del tablero actual.

        Returns:
            La instancia del tablero actualizada después del paso.
        """
        start_time = time.time()

        # 1. Calcular la próxima generación
        next_state = self._game_simulation_port.calculate_next_generation(board)

        # 2. Aplicar la próxima generación
        updated_board = self._game_simulation_port.apply_next_generation(
            board, next_state
        )

        end_time = time.time()
        step_time_ms = (end_time - start_time) * 1000

        # 3. Notificar a otros slices (ej. Estadísticas, Visualización)
        # Esto se haría a través de puertos secundarios o un sistema de eventos.
        # Por ahora, solo imprimimos el tiempo.
        print(f"Paso de simulación completado en {step_time_ms:.2f} ms.")

        # Notificar a Estadísticas (cuando el slice de Estadísticas esté implementado)
        # if self._simulation_step_notification_port:
        #     self._simulation_step_notification_port.notify_step_completed(updated_board, step_time_ms)

        return updated_board
