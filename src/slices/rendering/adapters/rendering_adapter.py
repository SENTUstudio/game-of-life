from src.slices.game_core.core.entities.board import (  # Usar importación absoluta
    Board,  # Necesitamos la instancia del tablero
)
from src.slices.rendering.core.rendering_config import (
    RenderingConfig,  # Necesitamos la instancia de configuración
)
from src.slices.rendering.core.use_cases.render_board_use_case import RenderBoardUseCase
from src.slices.rendering.core.use_cases.update_rendering_config_use_case import (
    UpdateRenderingConfigUseCase,
)
from src.slices.rendering.ports.primary_ports.rendering_port import IRenderingPort


class RenderingAdapter(IRenderingPort):
    """
    Adaptador que implementa el puerto primario IRenderingPort
    y delega las llamadas a los casos de uso correspondientes.
    """

    def __init__(
        self,
        render_board_use_case: RenderBoardUseCase,
        update_rendering_config_use_case: UpdateRenderingConfigUseCase,
        rendering_config: RenderingConfig,  # Inyectar la instancia de configuración
    ):
        """
        Inicializa el adaptador con las dependencias de casos de uso y configuración.
        """
        self._render_board_use_case = render_board_use_case
        self._update_rendering_config_use_case = update_rendering_config_use_case
        self._rendering_config = rendering_config

    # Implementación de IRenderingPort
    def render(self, board: Board) -> None:
        """
        Delega la solicitud de renderización al caso de uso correspondiente.
        """
        self._render_board_use_case.execute(board, self._rendering_config)

    def update_config(self, **kwargs):
        """
        Delega la actualización de la configuración al caso de uso correspondiente.
        """
        self._update_rendering_config_use_case.execute(**kwargs)
