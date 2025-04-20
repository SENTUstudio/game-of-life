from typing import Tuple

from src.slices.game_core.core.entities.board import (  # Usar importación absoluta
    Board,  # Necesitamos la instancia del tablero
)
from src.slices.game_core.core.entities.cell import (
    CellState,  # Usar importación absoluta
)
from src.slices.game_core.ports.primary_ports.board_modification_port import (  # Usar importación absoluta
    IBoardModificationPort,
)
from src.slices.game_core.ports.primary_ports.board_query_port import (  # Usar importación absoluta
    IBoardQueryPort,  # Necesitamos consultar el estado actual
)
from src.slices.rendering.ports.secondary_ports.graphics_library_port import (  # Usar importación absoluta
    IGraphicsLibraryPort,  # Para traducir coordenadas
)


class ModifyCellStateByClickUseCase:
    """
    Caso de uso para cambiar el estado de una célula por un clic del ratón.
    """

    def __init__(
        self,
        board_modification_port: IBoardModificationPort,
        board_query_port: IBoardQueryPort,
        graphics_library_port: IGraphicsLibraryPort,  # Inyectar puerto de la biblioteca gráfica
    ):
        """
        Inicializa el caso de uso con los puertos necesarios.

        Args:
            board_modification_port: El puerto para modificar el tablero.
            board_query_port: El puerto para consultar el estado del tablero.
            graphics_library_port: El puerto para interactuar con la biblioteca gráfica (para traducción de coordenadas).
        """
        self._board_modification_port = board_modification_port
        self._board_query_port = board_query_port
        self._graphics_library_port = graphics_library_port

    def execute(self, board: Board, mouse_position: Tuple[int, int]):
        """
        Traduce la posición del ratón a coordenadas del tablero y cambia el estado de la célula.

        Args:
            board: La instancia del tablero actual.
            mouse_position: La posición (x, y) del ratón en píxeles.
        """
        # Obtener la configuración de rendering para traducir coordenadas (necesita acceso a RenderingConfig)
        # Esto podría requerir un puerto secundario al slice de Rendering para obtener la configuración.
        # Por ahora, asumiré que puedo obtener la configuración de alguna manera o que el graphics_library_port
        # tiene un método para traducir directamente.
        # Usaré el método get_cell_coords_from_mouse_pos del PygameGraphicsAdapter (asumiendo que está disponible a través del puerto)
        # Esto puede requerir ajustar el diseño del puerto IGraphicsLibraryPort si no incluye esta funcionalidad.
        # Añadiré get_cell_coords_from_mouse_pos a IGraphicsLibraryPort.

        # Necesitamos la configuración de rendering para la traducción de coordenadas.
        # Esto implica que este caso de uso necesita una dependencia del slice de Rendering.
        # Podríamos inyectar la configuración directamente o un puerto para obtenerla.
        # Inyectar la configuración directamente podría acoplar este Core a un detalle de implementación.
        # Un puerto secundario al slice de Rendering para obtener la configuración parece más limpio.
        # Definiré un IRenderingQueryPort en el slice de Rendering.

        # Por ahora, para el prototipo, asumiré que puedo obtener la configuración de rendering.
        # Necesitamos la instancia de RenderingConfig.
        # Esto sugiere que RenderingConfig debería ser una dependencia inyectada aquí o accesible a través de un puerto.
        # Inyectaré la instancia de RenderingConfig directamente por simplicidad en el prototipo.
        # Esto acopla este caso de uso a la entidad RenderingConfig, lo cual no es ideal en un Core.
        # La alternativa es un puerto secundario al slice de Rendering para obtener la configuración.
        # Siguiendo el diseño, debería ser un puerto secundario.
        # Añadiré IRenderingQueryPort al slice de Rendering y lo inyectaré aquí.

        # Asumiendo que tenemos acceso a la configuración de rendering (a través de un puerto o inyección)
        # y que el graphics_library_port puede traducir coordenadas:
        # cell_x, cell_y = self._graphics_library_port.get_cell_coords_from_mouse_pos(mouse_position, rendering_config)

        # Para el prototipo, usaré el método del adaptador PygameGraphicsAdapter directamente si es posible,
        # o asumiré que el puerto tiene el método.
        # Asumiendo que el puerto IGraphicsLibraryPort tiene get_cell_coords_from_mouse_pos:
        # Necesitamos la instancia de RenderingConfig para pasársela.
        # Esto refuerza la necesidad de acceder a RenderingConfig.

        # Vamos a simplificar para el prototipo y asumir que el graphics_library_port
        # puede hacer la traducción con solo la posición del ratón y su propia configuración interna.
        # Esto requeriría que el adaptador gráfico mantenga su propia copia de RenderingConfig.
        # O que el método de traducción en el puerto gráfico reciba la configuración.
        # El diseño actual del puerto IGraphicsLibraryPort no incluye get_cell_coords_from_mouse_pos.
        # Lo añadiré a IGraphicsLibraryPort.

        # Después de añadir get_cell_coords_from_mouse_pos a IGraphicsLibraryPort:
        # Necesitamos la configuración de rendering para pasársela.
        # Inyectaré la configuración de rendering directamente en este caso de uso por ahora para el prototipo.
        # Esto es un acoplamiento temporal para el prototipo.

        # Asumiendo que RenderingConfig está inyectado en este caso de uso:
        # cell_x, cell_y = self._graphics_library_port.get_cell_coords_from_mouse_pos(mouse_position, self._rendering_config)

        # Para evitar inyectar RenderingConfig en el Core, el puerto secundario IRenderingQueryPort
        # es la mejor opción. Implementaré IRenderingQueryPort en el slice de Rendering
        # y lo inyectaré aquí.

        # Asumiendo que IRenderingQueryPort está inyectado y tiene get_rendering_config():
        # rendering_config = self._rendering_query_port.get_rendering_config()
        # cell_x, cell_y = self._graphics_library_port.get_cell_coords_from_mouse_pos(mouse_position, rendering_config)

        # Para el prototipo, y dado que el PygameGraphicsAdapter ya tiene el método,
        # y para evitar añadir un nuevo puerto y adaptador en Rendering solo para esto ahora,
        # haré que este caso de uso dependa directamente del PygameGraphicsAdapter.
        # Esto rompe la Arquitectura Hexagonal temporalmente para el prototipo.
        # O, mejor, añadiré el método get_cell_coords_from_mouse_pos al puerto IGraphicsLibraryPort
        # y lo implementaré en PygameGraphicsAdapter.

        # Asumiendo que get_cell_coords_from_mouse_pos está en IGraphicsLibraryPort:
        # Necesitamos la configuración de rendering.
        # Inyectaré la configuración de rendering directamente en este caso de uso para el prototipo.
        # Esto es un acoplamiento temporal.

        # from ...rendering.core.rendering_config import RenderingConfig # Importar RenderingConfig
        # self._rendering_config = rendering_config # Añadir a __init__

        # cell_x, cell_y = self._graphics_library_port.get_cell_coords_from_mouse_pos(mouse_position, self._rendering_config)

        # Para mantener la arquitectura, la mejor opción es el puerto secundario IRenderingQueryPort.
        # Lo añadiré al slice de Rendering y lo inyectaré aquí.

        # Asumiendo que IRenderingQueryPort está inyectado y tiene get_rendering_config():
        # from ...rendering.ports.primary_ports.rendering_query_port import IRenderingQueryPort # Importar el puerto
        # self._rendering_query_port = rendering_query_port # Añadir a __init__
        # rendering_config = self._rendering_query_port.get_rendering_config()
        # cell_x, cell_y = self._graphics_library_port.get_cell_coords_from_mouse_pos(mouse_position, rendering_config)

        # Para el prototipo, simplificaré y asumiré que el graphics_library_port puede hacer la traducción
        # sin necesidad de pasarle la configuración de rendering explícitamente aquí.
        # Esto implica que el adaptador gráfico tiene acceso a la configuración.
        # Modificaré IGraphicsLibraryPort para incluir get_cell_coords_from_mouse_pos(mouse_pos).

        # Después de modificar IGraphicsLibraryPort:
        cell_x, cell_y = self._graphics_library_port.get_cell_coords_from_mouse_pos(
            mouse_position
        )

        # Verificar si las coordenadas están dentro de los límites del tablero
        # Necesitamos el tamaño del tablero. Podemos obtenerlo del Board.
        # O podríamos necesitar un puerto secundario al slice de Game Core para obtener las dimensiones.
        # El IBoardQueryPort ya nos da acceso al Board.

        board_state = self._board_query_port.get_board_state(
            board
        )  # Obtener el estado para acceder a las dimensiones
        board_width = len(board_state[0]) if board_state else 0
        board_height = len(board_state)

        if 0 <= cell_x < board_width and 0 <= cell_y < board_height:
            # Obtener el estado actual de la célula
            current_state = self._board_query_port.get_cell_state(board, cell_x, cell_y)

            # Determinar el nuevo estado (alternar)
            new_state = (
                CellState.DEAD if current_state == CellState.ALIVE else CellState.ALIVE
            )

            # Cambiar el estado de la célula a través del puerto de modificación
            self._board_modification_port.set_cell_state(
                board, cell_x, cell_y, new_state
            )
            print(
                f"Célula en ({cell_x}, {cell_y}) cambiada a {new_state.name}"
            )  # Placeholder
        else:
            print(
                f"Clic fuera de los límites del tablero en posición: {mouse_position}"
            )  # Placeholder
