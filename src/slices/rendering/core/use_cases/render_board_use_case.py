from src.slices.game_core.core.entities.board import (  # Usar importación absoluta
    Board,  # Necesitamos la instancia del tablero
)
from src.slices.rendering.core.rendering_config import (
    RenderingConfig,  # Usar importación absoluta
)
from src.slices.rendering.ports.secondary_ports.graphics_library_port import (
    IGraphicsLibraryPort,  # Usar importación absoluta
)

# from src.slices.rendering.game_core.ports.primary_ports.board_query_port import IBoardQueryPort # Necesitamos este puerto para obtener el estado del tablero


class RenderBoardUseCase:
    """
    Caso de uso para renderizar el tablero del Juego de la Vida.
    """

    def __init__(
        self,
        graphics_library_port: IGraphicsLibraryPort,
        # board_query_port: IBoardQueryPort # Inyectar puerto de consulta del tablero
    ):
        """
        Inicializa el caso de uso con el puerto de la biblioteca gráfica.

        Args:
            graphics_library_port: El puerto para interactuar con la biblioteca gráfica.
            # board_query_port: El puerto para obtener el estado del tablero.
        """
        self._graphics_library_port = graphics_library_port
        # self._board_query_port = board_query_port

    def execute(self, board: Board, config: RenderingConfig):
        """
        Renderiza el tablero en la superficie de visualización.

        Args:
            board: La instancia del tablero actual.
            config: La configuración de visualización actual.
        """
        # Obtener el estado del tablero (cuando el puerto esté inyectado)
        # board_state = self._board_query_port.get_board_state(board)

        # Usar el adaptador gráfico para dibujar
        self._graphics_library_port.draw_board(
            board, config
        )  # Pasamos el board directamente por ahora
        self._graphics_library_port.update_display()  # Actualizar la pantalla
