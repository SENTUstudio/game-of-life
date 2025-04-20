class SimulationMetrics:
    """
    Clase que almacena las métricas de la simulación.

    Attributes:
        generation (int): Número de generación actual.
        alive (int): Número de células vivas.
        step_time (float): Tiempo de cálculo de la última generación en milisegundos.
    """

    def __init__(self):
        """Inicializa las métricas con valores por defecto."""
        self.generation = 0
        self.alive = 0
        self.step_time = 0.0

    def update(self, generation: int, alive: int, step_time: float) -> None:
        """
        Actualiza las métricas con nuevos valores.

        Args:
            generation: Número de generación actual.
            alive: Número de células vivas.
            step_time: Tiempo de cálculo de la última generación en milisegundos.

        Returns:
            None
        """
        self.generation = generation
        self.alive = alive
        self.step_time = step_time
