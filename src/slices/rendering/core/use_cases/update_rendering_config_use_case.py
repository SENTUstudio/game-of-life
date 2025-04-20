from src.slices.rendering.core.rendering_config import RenderingConfig


class UpdateRenderingConfigUseCase:
    """
    Caso de uso para actualizar la configuración de visualización.
    """

    def __init__(self, rendering_config: RenderingConfig):
        """
        Inicializa el caso de uso con la instancia de configuración de visualización.

        Args:
            rendering_config: La instancia de la configuración de visualización.
        """
        self._rendering_config = rendering_config

    def execute(self, **kwargs):
        """
        Actualiza la configuración de visualización con los valores proporcionados.

        Args:
            **kwargs: Argumentos clave-valor para actualizar la configuración.
        """
        self._rendering_config.update(**kwargs)
        print("Configuración de rendering actualizada.")  # Placeholder para feedback
