class SimulationMetricsAdapter:
    """
    Adaptador para las métricas de simulación.
    """

    def __init__(self, simulation_metrics):
        """
        Inicializa el adaptador con una instancia de SimulationMetrics.

        Args:
            simulation_metrics: Instancia de SimulationMetrics.
        """
        self._metrics = simulation_metrics

    @property
    def generation(self):
        """Obtiene el número de generación actual."""
        return self._metrics.generation

    @property
    def alive(self):
        """Obtiene el número de células vivas."""
        return self._metrics.alive

    @property
    def step_time(self):
        """Obtiene el tiempo del último paso en milisegundos."""
        return self._metrics.step_time
