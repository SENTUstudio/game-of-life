class SimulationMetrics:
    """
    Clase que almacena las métricas de la simulación.
    """

    def __init__(self):
        print("DEBUG: SimulationMetrics correcto importado desde", __file__)
        self.generation = 0
        self.alive = 0
        self.step_time = 0.0

    def update(self, generation: int, alive: int, step_time: float):
        """
        Actualiza las métricas con nuevos valores.

        Args:
            generation: Número de generación actual.
            alive: Número de células vivas.
            step_time: Tiempo de cálculo de la última generación en milisegundos.
        """
        self.generation = generation
        self.alive = alive
        self.step_time = step_time
