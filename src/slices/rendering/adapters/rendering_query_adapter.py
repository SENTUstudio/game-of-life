from typing import Tuple

from src.slices.rendering.core.rendering_config import (
    RenderingConfig,  # Usar importación absoluta
)
from src.slices.rendering.ports.primary_ports.rendering_query_port import (
    IRenderingQueryPort,  # Usar importación absoluta
)
from src.slices.rendering.ports.secondary_ports.graphics_library_port import (  # Usar importación absoluta
    IGraphicsLibraryPort,  # Necesitamos el puerto gráfico para la traducción de coordenadas
)


class RenderingQueryAdapter(IRenderingQueryPort):
    """
    Adaptador que implementa el puerto primario IRenderingQueryPort
    y proporciona acceso a la configuración de rendering y traducción de coordenadas.
    """

    def __init__(
        self,
        rendering_config: RenderingConfig,
        graphics_library_port: IGraphicsLibraryPort,
    ):
        """
        Inicializa el adaptador con la configuración de rendering y el puerto gráfico.

        Args:
            rendering_config: La instancia de la configuración de visualización.
            graphics_library_port: El puerto para interactuar con la biblioteca gráfica.
        """
        self._rendering_config = rendering_config
        self._graphics_library_port = graphics_library_port

    # Implementación de IRenderingQueryPort
    def get_rendering_config(self) -> RenderingConfig:
        """
        Retorna la configuración de visualización actual.
        """
        return self._rendering_config

    def get_cell_coords_from_mouse_pos(
        self, mouse_pos: Tuple[int, int]
    ) -> Tuple[int, int]:
        """
        Delega la traducción de la posición del ratón a coordenadas de celda al adaptador gráfico.
        """
        # Asumimos que el graphics_library_port tiene este método y puede usar su configuración interna
        # o que le pasamos la configuración aquí.
        # Basado en la modificación anterior de IGraphicsLibraryPort, el método en el puerto
        # ahora solo recibe mouse_pos.
        return self._graphics_library_port.get_cell_coords_from_mouse_pos(mouse_pos)
