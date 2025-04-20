class SimulationMetrics:
    """
    Representa las métricas de la simulación del Juego de la Vida.
    """

    def __init__(
        self,
        generation_count: int = 0,
        live_cell_count: int = 0,
        step_time_ms: float = 0.0,
    ):
        """
        Inicializa las métricas de simulación.

        Args:
            generation_count: Número de la generación actual.
            live_cell_count: Número de células vivas.
            step_time_ms: Tiempo que tomó el último paso en milisegundos.
        """
        self.generation_count = generation_count
        self.live_cell_count = live_cell_count
        self.step_time_ms = step_time_ms

    def update(self, generation_count: int, live_cell_count: int, step_time_ms: float):
        """
        Actualiza las métricas.

        Args:
            generation_count: Nuevo número de la generación actual.
            live_cell_count: Nuevo número de células vivas.
            step_time_ms: Nuevo tiempo que tomó el último paso en milisegundos.
        """
        self.generation_count = generation_count
        self.live_cell_count = live_cell_count
        self.step_time_ms = step_time_ms

    def __repr__(self) -> str:
        """
        Representación de cadena de las métricas.
        """
        return f"SimulationMetrics(generation={self.generation_count}, alive={self.live_cell_count}, step_time={self.step_time_ms:.2f}ms)"
