from src.slices.game_core.core.entities.board import (  # Usar importación absoluta
    Board,  # Necesitamos la instancia del tablero
)
from src.slices.game_core.ports.primary_ports.board_query_port import (  # Usar importación absoluta
    IBoardQueryPort,  # Necesitamos consultar el estado del tablero
)
from src.slices.statistics.core.entities.simulation_metrics import SimulationMetrics


class UpdateStatisticsUseCase:
    """
    Caso de uso para actualizar las estadísticas de la simulación.
    """

    def __init__(
        self, simulation_metrics: SimulationMetrics, board_query_port: IBoardQueryPort
    ):
        """
        Inicializa el caso de uso con las métricas de simulación y el puerto de consulta del tablero.

        Args:
            simulation_metrics: La instancia de las métricas de simulación.
            board_query_port: El puerto para consultar el estado del tablero.
        """
        self._simulation_metrics = simulation_metrics
        self._board_query_port = board_query_port

    def execute(self, board: Board, step_time_ms: float):
        """
        Recalcula y actualiza las métricas de la simulación.

        Args:
            board: La instancia del tablero actual.
            step_time_ms: El tiempo que tomó el último paso en milisegundos.
        """
        # Obtener el estado del tablero para contar células vivas
        board_state = self._board_query_port.get_board_state(board)
        live_cell_count = sum(
            row.count(1) for row in board_state
        )  # Contar células vivas (asumiendo 1 para ALIVE)

        # Incrementar el contador de generación
        new_generation_count = self._simulation_metrics.generation_count + 1

        # Actualizar las métricas
        self._simulation_metrics.update(
            new_generation_count, live_cell_count, step_time_ms
        )
        print(
            f"Estadísticas actualizadas: {self._simulation_metrics}"
        )  # Placeholder para feedback
